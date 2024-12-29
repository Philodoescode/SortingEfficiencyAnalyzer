import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from controller import Controller
import sorting_algorithms
import random
from graphGUI import *
class InputUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Input Handler UI")

        self.current_page = 0

        self.array = []
        self.shuffle_type = None
        self.input_type = None
        self.sorting_algorithm_1 = None
        self.sorting_algorithm_2 = None

        self.pages = []

        self.create_pages()
        self.show_page(0)

    def create_pages(self):
        self.create_comparison_page()
        self.create_input_page()

    def toggle_input_mode(self):
        """Toggles visibility of CSV input and array creation frames."""
        if self.input_mode_var.get() == "csv":
            self.csv_frame.grid(row=1, column=1, rowspan=2, padx=10, pady=5, sticky="w")
            self.array_frame.grid_forget()
        else:
            self.array_frame.grid(row=1, column=1, rowspan=2, padx=10, pady=5, sticky="w")
            self.csv_frame.grid_forget()

    def create_input_page(self):
        frame = tk.Frame(self.root)
        self.pages.append(frame)

        input_mode_label = tk.Label(frame, text="Input Mode:")
        input_mode_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.input_mode_var = tk.StringVar(value="array")
        csv_radio = tk.Radiobutton(frame, text="Load from CSV", variable=self.input_mode_var, value="csv", command=self.toggle_input_mode)
        csv_radio.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        array_radio = tk.Radiobutton(frame, text="Create Array", variable=self.input_mode_var, value="array", command=self.toggle_input_mode)
        array_radio.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # CSV input
        self.csv_frame = tk.Frame(frame)
        csv_label = tk.Label(self.csv_frame, text="CSV File Path:")
        csv_label.grid(row=0, column=0, padx=5, pady=5)

        self.csv_path_entry = tk.Entry(self.csv_frame, width=40)
        self.csv_path_entry.grid(row=0, column=1, padx=5, pady=5)

        browse_button = tk.Button(self.csv_frame, text="Browse", command=self.browse_file)
        browse_button.grid(row=0, column=2, padx=5, pady=5)

        # Array creation
        self.array_frame = tk.Frame(frame)

        size_label = tk.Label(self.array_frame, text="Array Size:")
        size_label.grid(row=0, column=0, padx=5, pady=5)

        self.size_var = tk.IntVar(value=10)
        size_slider = tk.Scale(self.array_frame, from_=20, to=500, orient=tk.HORIZONTAL, variable=self.size_var, command=self.update_size_entry)
        size_slider.grid(row=0, column=1, padx=5, pady=5)

        self.size_entry = tk.Entry(self.array_frame, width=10)
        self.size_entry.insert(0, "20")
        self.size_entry.grid(row=0, column=2, padx=5, pady=5)

        ok_button = tk.Button(self.array_frame, text="OK", command=self.update_size_slider)
        ok_button.grid(row=0, column=3, padx=5, pady=5)

        shuffle_label = tk.Label(self.array_frame, text="Shuffle Type:")
        shuffle_label.grid(row=1, column=0, padx=5, pady=5)

        self.shuffle_var = tk.StringVar(value="Randomized")
        shuffle_menu = ttk.Combobox(self.array_frame, textvariable=self.shuffle_var, values=["Reverse sorted", "Randomized", "Semi-sorted", "Fully-sorted"], state="readonly")
        shuffle_menu.grid(row=1, column=1, padx=5, pady=5)

        input_type_label = tk.Label(self.array_frame, text="Input Type:")
        input_type_label.grid(row=2, column=0, padx=5, pady=5)

        self.input_type_var = tk.StringVar(value="Contiguous values")
        input_type_menu = ttk.Combobox(self.array_frame, textvariable=self.input_type_var, values=["Contiguous values", "Non-contiguous values"], state="readonly")
        input_type_menu.grid(row=2, column=1, padx=5, pady=5)

        self.toggle_input_mode()

        back_button = tk.Button(frame, text="Back", command=lambda: self.show_page(0))
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        run_button = tk.Button(frame, text="Run", command=self.run)
        run_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")


    def create_comparison_page(self):
        frame = tk.Frame(self.root)
        self.pages.append(frame)

        compare_mode_label = tk.Label(frame, text="Comparison Mode:")
        compare_mode_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.compare_mode_var = tk.StringVar(value="single")
        single_algo_radio = tk.Radiobutton(frame, text="Compare with Asymptotic Efficiency", variable=self.compare_mode_var, value="single", command=self.toggle_comparison_mode)
        single_algo_radio.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        double_algo_radio = tk.Radiobutton(frame, text="Compare Two Algorithms", variable=self.compare_mode_var, value="double", command=self.toggle_comparison_mode)
        double_algo_radio.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        algorithm_list = [
            "Quick Sort", "Merge Sort", "Shell Sort", "Selection Sort",
            "Insertion Sort", "Heap Sort", "Gnome Sort", "Odd-Even Sort",
            "Bubble Sort", "Cocktail Shaker Sort", "Counting Sort",
            "Bucket Sort", "Radix Sort", "Gravity Sort (Bead Sort)"
        ]

        sorting_label_1 = tk.Label(frame, text="Algorithm 1:")
        sorting_label_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.sorting_var_1 = tk.StringVar(value="Quick Sort")
        self.sorting_menu_1 = ttk.Combobox(frame, textvariable=self.sorting_var_1, values=algorithm_list, state="readonly")
        self.sorting_menu_1.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.sorting_label_2 = tk.Label(frame, text="Algorithm 2:")
        self.sorting_label_2.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.sorting_var_2 = tk.StringVar(value="Merge Sort")
        self.sorting_menu_2 = ttk.Combobox(frame, textvariable=self.sorting_var_2, values=algorithm_list, state="readonly")
        self.sorting_menu_2.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        next_button = tk.Button(frame, text="Next", command=lambda: self.show_page(1))
        next_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        self.sorting_var_1.trace_add("write", self.ensure_different_algorithms)
        self.sorting_var_2.trace_add("write", self.ensure_different_algorithms)

        self.toggle_comparison_mode()

    def toggle_comparison_mode(self):
        if self.compare_mode_var.get() == "single":
            self.sorting_label_2.grid_remove()
            self.sorting_menu_2.grid_remove()
        else:
            self.sorting_label_2.grid()
            self.sorting_menu_2.grid()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[["CSV files", "*.csv"]])
        if file_path:
            self.csv_path_entry.delete(0, tk.END)
            self.csv_path_entry.insert(0, file_path)

    def update_size_entry(self, value):
        self.size_entry.delete(0, tk.END)
        self.size_entry.insert(0, str(self.size_var.get()))

    def update_size_slider(self):
        try:
            size = int(self.size_entry.get())
            if 20 <= size <= 500:
                self.size_var.set(size)
            else:
                messagebox.showerror("Error", "Size must be between 20 and 500.")
        except ValueError:
            messagebox.showerror("Error", "Invalid size. Please enter a valid number.")

    def ensure_different_algorithms(self, *args):
        if self.sorting_var_1.get() == self.sorting_var_2.get() and self.compare_mode_var.get() == "double":
            available_algorithms = [
                "Quick Sort", "Merge Sort", "Shell Sort", "Selection Sort",
                "Insertion Sort", "Heap Sort", "Gnome Sort", "Odd-Even Sort",
                "Bubble Sort", "Cocktail Shaker Sort", "Counting Sort",
                "Bucket Sort", "Radix Sort", "Gravity Sort (Bead Sort)"
            ]
            available_algorithms.remove(self.sorting_var_1.get())
            self.sorting_var_2.set(available_algorithms[0])
            messagebox.showwarning("Warning", "Algorithms cannot be the same.")



    def run(self):
        input_handler = Controller()

        if self.compare_mode_var.get() == "double" and self.sorting_var_1.get() == self.sorting_var_2.get():
            messagebox.showerror("Error", "Please select two different sorting algorithms.")
            return

        if self.input_mode_var.get() == "csv":
            file_path = self.csv_path_entry.get()
            try:
                self.array = input_handler.load_csv(file_path)


                messagebox.showinfo("Success", f"Array loaded successfully: {self.array}")
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV file: {e}")
        else:
            size = self.size_var.get()
            shuffle_type = self.shuffle_var.get()
            input_type = self.input_type_var.get()

            try:
                self.array = input_handler.generate_array(size, shuffle_type, input_type)
                print(self.array)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate array: {e}")

        if self.compare_mode_var.get() == "single":
            self.sorting_algorithm_1 = self.sorting_var_1.get()
            sizes, steps_selected, steps_worst, steps_best, times1, times_worst, times_best = self.perform_single_comparison()
            self.show_graph_gui_single(sizes, steps_selected, steps_worst, steps_best, times1, times_worst, times_best)
        elif self.compare_mode_var.get() == "double":
            self.sorting_algorithm_1 = self.sorting_var_1.get()
            self.sorting_algorithm_2 = self.sorting_var_2.get()
            sizes1, steps1, sizes2, steps2, times1, times2 = self.perform_algorithm_comparison()
            self.show_graph_gui(sizes1, steps1, sizes2, steps2, times1, times2)

    def perform_single_comparison(self):
        sizes = []
        steps_selected = []
        steps_worst = []
        steps_best = []
        times1 = []
        times_worst = []
        times_best = []
        input_handler = Controller()
        shuffle_type = self.shuffle_var.get()
        input_type = self.input_type_var.get()


        for i in range(10, len(self.array) + 1, 3):
            # Selected shuffle type
            sizes.append(i)
            temp_array = self.array[0:i]
            start_time = time.perf_counter()
            sorting_algorithms.SortingAlgorithms.step_counter = 0
            getattr(sorting_algorithms.SortingAlgorithms, self.sorting_algorithm_1.lower().replace(" ", "_"))(temp_array)
            end_time = time.perf_counter()
            steps_selected.append(sorting_algorithms.SortingAlgorithms.step_counter)
            times1.append(end_time - start_time)

            # Worst-case scenario (reverse sorted array)
            worst_array = list(range(i, 0, -1))
            start_time = time.perf_counter()
            sorting_algorithms.SortingAlgorithms.step_counter = 0
            getattr(sorting_algorithms.SortingAlgorithms, self.sorting_algorithm_1.lower().replace(" ", "_"))(worst_array)
            steps_worst.append(sorting_algorithms.SortingAlgorithms.step_counter)
            end_time = time.perf_counter()
            times_worst.append(end_time - start_time)

            # Best-case scenario (already sorted array)
            best_array = list(range(i))
            start_time = time.perf_counter()
            sorting_algorithms.SortingAlgorithms.step_counter = 0
            getattr(sorting_algorithms.SortingAlgorithms, self.sorting_algorithm_1.lower().replace(" ", "_"))(best_array)
            steps_best.append(sorting_algorithms.SortingAlgorithms.step_counter)
            end_time = time.perf_counter()
            times_best.append(end_time - start_time)

        return sizes, steps_selected, steps_worst, steps_best, times1, times_worst, times_best

    def perform_algorithm_comparison(self):
        sizes1, steps1, times1 = [], [], []
        sizes2, steps2, times2 = [], [], []
        input_handler = Controller()

        for i in range(10, len(self.array) + 1, 3):
            # Algorithm 1
            sizes1.append(i)
            temp_array = self.array[0:i]

            start_time = time.perf_counter()
            sorting_algorithms.SortingAlgorithms.step_counter = 0
            getattr(sorting_algorithms.SortingAlgorithms, self.sorting_algorithm_1.lower().replace(" ", "_"))(temp_array)
            steps1.append(sorting_algorithms.SortingAlgorithms.step_counter)
            end_time = time.perf_counter()
            times1.append(end_time - start_time)

            # Algorithm 2
            sizes2.append(i)
            temp_array = self.array[0:i]
            start_time = time.perf_counter()
            sorting_algorithms.SortingAlgorithms.step_counter = 0
            getattr(sorting_algorithms.SortingAlgorithms, self.sorting_algorithm_2.lower().replace(" ", "_"))(temp_array)
            steps2.append(sorting_algorithms.SortingAlgorithms.step_counter)
            end_time = time.perf_counter()
            times2.append(end_time - start_time)

        return sizes1, steps1, sizes2, steps2, times1, times2

    def show_graph_gui(self, sizes1, steps1, sizes2, steps2, times1, times2):
        # Steps graph
        new_window_steps = tk.Toplevel(self.root)
        GraphPlaceholderApp(new_window_steps, sizes1, steps1, sizes2, steps2,
                            label1=f"{self.sorting_algorithm_1} Steps",
                            label2=f"{self.sorting_algorithm_2} Steps",
                            graph_title="Comparison of Steps Taken")

        # Time graph
        new_window_time = tk.Toplevel(self.root)
        GraphPlaceholderApp(new_window_time, sizes1, times1, sizes2, times2,
                            label1=f"{self.sorting_algorithm_1} Time",
                            label2=f"{self.sorting_algorithm_2} Time",
                            graph_title="Comparison of Time Taken")

    def show_graph_gui_single(self, sizes, steps_selected, steps_worst, steps_best, times1, times_worst, times_best):
        # Steps graph
        new_window_steps = tk.Toplevel(self.root)
        GraphPlaceholderApp(new_window_steps, sizes, steps_selected, sizes, steps_worst, sizes, steps_best,
                            label1=f"{self.sorting_algorithm_1} ({self.shuffle_var.get()}) Steps",
                            label2=f"{self.sorting_algorithm_1} (reverse sorted) Steps",
                            label3=f"{self.sorting_algorithm_1} (sorted) Steps",
                            graph_title="Comparison of Steps Taken (Single)")

        # Time graph
        new_window_time = tk.Toplevel(self.root)
        GraphPlaceholderApp(new_window_time, sizes, times1, sizes, times_worst, sizes, times_best,
                            label1=f"{self.sorting_algorithm_1} ({self.shuffle_var.get()}) Time",
                            label2=f"{self.sorting_algorithm_1} (reverse sorted) Time",
                            label3=f"{self.sorting_algorithm_1} (sorted) Time",
                            graph_title="Comparison of Time Taken (Single)")



    def show_page(self, page_index):
        for i, page in enumerate(self.pages):
            if i == page_index:
                page.pack(fill="both", expand=True)
            else:
                page.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    app = InputUI(root)
    root.mainloop()