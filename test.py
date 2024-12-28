import csv
import random

# Function to generate a CSV file with a randomly sorted array
def generate_random_array_csv(filename, size):
    random_array = random.sample(range(1, size + 1), size)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(random_array)
    return filename

# Generate a CSV file with a randomly sorted array of size 100
csv_file = generate_random_array_csv("random_array.csv", 100)
csv_file
