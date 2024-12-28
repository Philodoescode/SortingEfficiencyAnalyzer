import csv
import random
import SortingAlgorithms
class Controller:
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
    
    def sort_array(self, algorithm_name):
        """Sorts the array using the selected algorithm."""
        if not self.array:
            raise ValueError("Array is empty. Please load or generate an array first.")
        
        algorithms = {
            "Merge Sort": SortingAlgorithms.merge_sort,
            "Shell Sort": SortingAlgorithms.shell_sort,
            "Selection Sort": SortingAlgorithms.selection_sort,
            "Insertion Sort": SortingAlgorithms.insertion_sort,
            "Heap Sort": SortingAlgorithms.heap_sort,
            "Gravity Sort": SortingAlgorithms.gravity_sort,
            "Bubble Sort": SortingAlgorithms.bubble_sort,
            "Cocktail Shaker Sort": SortingAlgorithms.cocktail_shaker_sort,
            "Counting Sort": SortingAlgorithms.counting_sort,
            "Radix Sort": SortingAlgorithms.radix_sort,
            "Gnome Sort": SortingAlgorithms.gnome_sort,
            "Odd-Even Sort": SortingAlgorithms.odd_even_sort,
        }

        algorithm = algorithms.get(algorithm_name)
        if not algorithm:
            raise ValueError(f"Algorithm '{algorithm_name}' not recognized.")

        # Reset metrics and sort
        SortingAlgorithms.metrics.reset()
        algorithm(self.array)

        # Output the sorted array and metrics
        print(f"Sorted Array using {algorithm_name}: {self.array}")
        print("Metrics:")
        print(f"Time Taken: {SortingAlgorithms.metrics.time_taken:.6f} seconds")
        print(f"Comparisons: {SortingAlgorithms.metrics.comparisons}")
        print(f"Swaps: {SortingAlgorithms.metrics.swaps}")
        print(f"Main Writes: {SortingAlgorithms.metrics.main_writes}")
        print(f"Auxiliary Writes: {SortingAlgorithms.metrics.aux_writes}")