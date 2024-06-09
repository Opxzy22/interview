from statistics import median
from collections import Counter
import psycopg2
from dotenv import load_dotenv
import os
import random


data = {
    "Monday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "Tuesday": ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    "Wednesday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    "Thursday": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "Friday": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
}

all_colors = [color for colors in data.values() for color in colors]

color_counts = Counter(all_colors)

color_counts = {}
# loop through all colors to get each color
for color in all_colors:
    # if color exist it should add +1
    if color in color_counts:
        color_counts[color] += 1
    # if color don't exist color equals 1
    else:
        color_counts[color] = 1
print(color_counts)

most_common_color = max(color_counts, key=color_counts.get)

print('mean color:', most_common_color)
print('most common color i:', most_common_color)

total_colors = len(all_colors)

red_count = color_counts.get("RED") 
probability_red = red_count / total_colors

print("Probability of Choosing Red:", probability_red)

conn = psycopg2.connect(
    dbname= os.environ.get('DB_NAME'),
    user= os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
)

# Create a cursor object
cur = conn.cursor()

# Create a table to store colors and frequencies if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color TEXT PRIMARY KEY,
        frequency INTEGER
    )
""")

# Insert colors and frequencies into the table
for color, frequency in color_counts.items():
    cur.execute("""
        INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)
    """, (color, frequency))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()


# Generate random 4-digit number of 0s and 1s
random_number = ''.join(random.choices(['0', '1'], k=4))

# Convert the generated number to base 10
decimal_number = int(random_number, 2)

print("Random 4-Digit Number (Binary):", random_number)
print("Converted to Base 10:", decimal_number)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

# Generate the first 50 Fibonacci numbers
fib_sequence = fibonacci(50)

# Sum the first 50 Fibonacci numbers
fib_sum = sum(fib_sequence)

print("Sum of the first 50 Fibonacci numbers:", fib_sum)

