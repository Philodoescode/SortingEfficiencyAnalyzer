import csv
import random
import sorting_algorithms

class Controller:
    def __init__(self):
        self.array = []
        self.metrics = sorting_algorithms.Metrics()  # Instance of Metrics

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

    def sort_array(self, comparison_mode, algorithm_name_1, algorithm_name_2=None):
        """Sorts the array based on the comparison mode and selected algorithms."""
        if not self.array:
            raise ValueError("Array is empty. Please load or generate an array first.")

        algorithms = {
            "Quick Sort": sorting_algorithms.SortingAlgorithms.quick_sort,
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

        metrics_1 = sorting_algorithms.Metrics()
        metrics_2 = sorting_algorithms.Metrics()

        if comparison_mode == "single":
            # Sort using the first algorithm
            algorithm = algorithms.get(algorithm_name_1)
            if not algorithm:
                raise ValueError(f"Algorithm '{algorithm_name_1}' not recognized.")
            algorithm(self.array, metrics_1)
            print(f"Sorted Array using {algorithm_name_1}: {self.array}")

        elif comparison_mode == "double":
            if not algorithm_name_2:
                raise ValueError("Second algorithm is required for double comparison mode.")

            # Save original array
            original_array = self.array.copy()

            # Sort using the first algorithm
            algorithm_1 = algorithms.get(algorithm_name_1)
            if not algorithm_1:
                raise ValueError(f"Algorithm '{algorithm_name_1}' not recognized.")
            algorithm_1(self.array, metrics_1)

            # Store the result for the first algorithm
            sorted_array_1 = self.array.copy()

            # Reset the array for the second algorithm
            self.array = original_array

            # Sort using the second algorithm
            algorithm_2 = algorithms.get(algorithm_name_2)
            if not algorithm_2:
                raise ValueError(f"Algorithm '{algorithm_name_2}' not recognized.")
            algorithm_2(self.array, metrics_2)

            # Store the result for the second algorithm
            sorted_array_2 = self.array.copy()

            print(f"Sorted Array using {algorithm_name_1}: {sorted_array_1}")
            print(f"Sorted Array using {algorithm_name_2}: {sorted_array_2}")

        else:
            raise ValueError("Invalid comparison mode. Use 'single' or 'double'.")

        # Output metrics
        print("\nMetrics for", algorithm_name_1, ":")
        print(f"Time Taken: {metrics_1.time_taken:.6f} seconds")
        print(f"Comparisons: {metrics_1.comparisons}")
        print(f"Swaps: {metrics_1.swaps}")
        print(f"Main Writes: {metrics_1.main_writes}")
        print(f"Auxiliary Writes: {metrics_1.aux_writes}")

        if comparison_mode == "double":
            print("\nMetrics for", algorithm_name_2, ":")
            print(f"Time Taken: {metrics_2.time_taken:.6f} seconds")
            print(f"Comparisons: {metrics_2.comparisons}")
            print(f"Swaps: {metrics_2.swaps}")
            print(f"Main Writes: {metrics_2.main_writes}")
            print(f"Auxiliary Writes: {metrics_2.aux_writes}")
