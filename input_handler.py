import csv
import random

class InputHandler:
    def __init__(self):
        self.array = []

    def load_csv(self, file_path):
        """Loads array data from a CSV file."""
        if not file_path.endswith('.csv'):
            raise ValueError("Invalid file type. Please select a CSV file.")
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            self.array = []
            for row in reader:
                self.array.extend(map(int, row))
        return self.array

    def generate_array(self, size, shuffle_type, input_type):
        """Generates an array based on input specifications."""
        if input_type == "Contiguous values":
            array = list(range(1, size + 1))
        elif input_type == "Non-contiguous values":
            array = [random.randint(1, size * 2) for _ in range(size)]

        if shuffle_type == "Reverse sorted":
            array.sort(reverse=True)
        elif shuffle_type == "Semi-sorted":
            split_point = size // 2
            array[:split_point] = sorted(array[:split_point])
            array[split_point:] = array[split_point:][::-1]
        elif shuffle_type == "Fully-sorted":
            array.sort()

        self.array = array
        return array
