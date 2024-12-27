import random
import csv

class InputHandler:
    def __init__(self):
        self.array = []
        self.comparison_choice = None
        self.selected_algorithms = []

    def get_valid_input(self, prompt, cast_func=str, condition=lambda x: True, error_message="Invalid input."):
        while True:
            try:
                value = cast_func(input(prompt).strip())
                if condition(value):
                    return value
                else:
                    print(error_message)
            except Exception as e:
                print(f"Error: {e}")

    def load_csv(self):
        while True:
            file_path = input("Enter the path to the CSV file: ").strip()
            try:
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    self.array = []
                    for row in reader:
                        self.array.extend(map(int, row))
                    print(f"Array loaded successfully: {self.array}")
                    return
            except Exception as e:
                print(f"Error loading file: {e}")

    def generate_array(self):
        size = self.get_valid_input("Enter the size of the array (must be at least 3): ", int, lambda x: x >= 3, "Size must be an integer greater than or equal to 3.")

        print("Sorting state options:")
        print("1. Reverse sorted")
        print("2. Randomized")
        print("3. Semi-sorted")
        print("4. Fully sorted")
        state = self.get_valid_input("Choose a sorting state (1-4): ", int, lambda x: x in range(1, 5))

        print("Input type options:")
        print("1. Contiguous values")
        print("2. Non-contiguous random values")
        input_type = self.get_valid_input("Choose an input type (1 or 2): ", int, lambda x: x in [1, 2])

        if input_type == 1:
            self.array = list(range(1, size + 1))
        else:
            self.array = [random.randint(1, size * 2) for _ in range(size)]

        if state == 1:
            self.array.sort(reverse=True)
        elif state == 3:
            split_point = size // 2
            self.array[:split_point] = sorted(self.array[:split_point])
            self.array[split_point:] = self.array[split_point:][::-1]
        elif state == 4:
            self.array.sort()

        print(f"Generated array: {self.array}")

    def choose_comparison(self):
        print("\nComparison Options")
        print("1. Compare two algorithms")
        print("2. Compare an algorithm against its asymptotic efficiency")

        self.comparison_choice = self.get_valid_input("Choose an option (1 or 2): ", int, lambda x: x in [1, 2])
        algorithms = [
            "Quick Sort", "Merge Sort", "Shell Sort", "Selection Sort", "Insertion Sort",
            "Heap Sort", "Gnome Sort", "Odd-Even Sort", "Bubble Sort", "Cocktail Shaker Sort",
            "Counting Sort", "Bucket Sort", "Radix Sort", "Gravity Sort (Bead Sort)"
        ]

        if self.comparison_choice == 1:
            print("Available Algorithms:")
            for i, algo in enumerate(algorithms, start=1):
                print(f"{i}. {algo}")

            first_algo = self.get_valid_input("Select the first algorithm (1-15): ", int, lambda x: 1 <= x <= len(algorithms))
            second_algo = self.get_valid_input("Select the second algorithm (1-15): ", int, lambda x: 1 <= x <= len(algorithms) and x != first_algo)

            self.selected_algorithms = [algorithms[first_algo - 1], algorithms[second_algo - 1]]

            print(f"Selected algorithms: {self.selected_algorithms[0]} and {self.selected_algorithms[1]}")
        else:
            print("Available Algorithms:")
            for i, algo in enumerate(algorithms, start=1):
                print(f"{i}. {algo}")

            algo_index = self.get_valid_input("Select an algorithm (1-15): ", int, lambda x: 1 <= x <= len(algorithms))
            self.selected_algorithms = [algorithms[algo_index - 1]]

            print(f"Selected algorithm: {self.selected_algorithms[0]} to compare against its asymptotic efficiency.")

    def summarize_choices(self):
        print("\nSummary of Choices:")
        print(f"Array: {self.array}")
        if self.comparison_choice == 1:
            print(f"Algorithms compared: {self.selected_algorithms[0]} and {self.selected_algorithms[1]}")
        else:
            print(f"Algorithm compared against asymptotic efficiency: {self.selected_algorithms[0]}")

if __name__ == "__main__":
    handler = InputHandler()
    print("\nArray Creation")
    print("1. Upload an external CSV file")
    print("2. Generate a computerized, randomized array")

    choice = handler.get_valid_input("Choose an option (1 or 2): ", int, lambda x: x in [1, 2])

    if choice == 1:
        handler.load_csv()
    else:
        handler.generate_array()

    handler.choose_comparison()
    handler.summarize_choices()