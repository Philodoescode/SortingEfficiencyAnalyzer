import csv
import random
import sorting_algorithms
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
            "Merge Sort": sorting_algorithms.SortingAlgorithms.merge_sort,
            "Shell Sort": sorting_algorithms.SortingAlgorithms.shell_sort,
            "Selection Sort": sorting_algorithms.SortingAlgorithms.selection_sort,
            "Insertion Sort": sorting_algorithms.SortingAlgorithms.insertion_sort,
            "Heap Sort": sorting_algorithms.SortingAlgorithms.heap_sort,
            "Gravity Sort": sorting_algorithms.SortingAlgorithms.gravity_sort,
            "Bubble Sort": sorting_algorithms.SortingAlgorithms.bubble_sort,
            "Cocktail Shaker Sort": sorting_algorithms.SortingAlgorithms.cocktail_shaker_sort,
            "Counting Sort": sorting_algorithms.SortingAlgorithms.counting_sort,
            "Radix Sort": sorting_algorithms.SortingAlgorithms.radix_sort,
            "Gnome Sort": sorting_algorithms.SortingAlgorithms.gnome_sort,
            "Odd-Even Sort": sorting_algorithms.SortingAlgorithms.odd_even_sort,
        }

        algorithm = algorithms.get(algorithm_name)
        if not algorithm:
            raise ValueError(f"Algorithm '{algorithm_name}' not recognized.")

        # Reset metrics and sort
        sorting_algorithms.Metrics.reset()
        algorithm(self.array)

        # Output the sorted array and metrics
        print(f"Sorted Array using {algorithm_name}: {self.array}")
        print("Metrics:")
        print(f"Time Taken: {sorting_algorithms.Metrics.time_taken:.6f} seconds")
        print(f"Comparisons: {sorting_algorithms.Metrics.comparisons}")
        print(f"Swaps: {sorting_algorithms.Metrics.swaps}")
        print(f"Main Writes: {sorting_algorithms.Metrics.main_writes}")
        print(f"Auxiliary Writes: {sorting_algorithms.Metrics.aux_writes}")