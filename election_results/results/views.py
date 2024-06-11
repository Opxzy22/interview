from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import PollingUnit, AnnouncedPUResults, LGA, AnnouncedPUResults

def polling_unit_results(request, polling_unit_id):
    results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid=polling_unit_id)
    context = {
        'results': results,
    }
    return render(request, 'results/polling_unit_results.html', context)

def lga_results(request):
    if request.method == 'POST':
        lga_id = request.POST.get('lga')
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)
        total_results = AnnouncedPUResults.objects.filter(
            polling_unit_uniqueid__in=[pu.uniqueid for pu in polling_units]
        ).values('party_abbreviation').annotate(total_score=Sum('party_score'))
        context = {
            'total_results': total_results,
            'lga_selected': True,
        }
    else:
        context = {
            'total_results': None,
            'lga_selected': False,
        }
    lgas = LGA.objects.all()
    context['lgas'] = lgas
    return render(request, 'results/lga_results.html', context)

def add_polling_unit_result(request):
    if request.method == 'POST':
        polling_unit_id = request.POST.get('polling_unit_id')
        party_scores = {
            'PDP': request.POST.get('pdp_score'),
            'ACN': request.POST.get('acn_score'),
            'DPP': request.POST.get('dpp_score'),
            'PPA': request.POST.get('ppa_score'),
            'CDC': request.POST.get('cdc_score'),
            'JP': request.POST.get('jp_score'),  
        }
        for party, score in party_scores.items():
            AnnouncedPUResults.objects.create(
                polling_unit_uniqueid=polling_unit_id,
                party_abbreviation=party,
                party_score=score
            )
        return redirect('success_page')
    return render(request, 'results/add_polling_unit_result.html')