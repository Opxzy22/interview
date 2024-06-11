from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit_results/', views.polling_unit_results, name='polling_unit_results'),
    path('lga_results/', views.lga_results, name='lga_results'),
    path('add_polling_unit_result/', views.add_polling_unit_result, name='add_polling_unit_result'),
]