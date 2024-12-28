import tkinter as tk
from tkinter import Frame
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class csvexport:
    def __init__(self, filename):
        self.filename = filename

    def export_to_csv(output_filename, size, elapsed_time):
        with open(output_filename, 'a') as output_file:  # Open file in append mode
            output_file.write(f"{size},{elapsed_time}\n")

class GraphPlaceholderApp:
    def __init__(self, master, x1, y1, x2, y2, label1, label2):
        self.master = master
        self.master.title("Graph Display")
        self.master.configure(bg="#87CEEB")  # Sky blue

        # Configure the window size
        self.master.geometry("800x600")

        # Create the main frame for the graph
        self.graph_frame = Frame(self.master, bg="#87CEEB")
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add the graph
        self.create_graph(x1, y1, x2, y2, label1, label2)

    def create_graph(self, x1, y1, x2, y2, label1, label2):
        # Create a Matplotlib figure and axis
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Plot the data
        ax.plot(x1, y1, label=label1, marker='o')
        ax.plot(x2, y2, label=label2, marker='s')

        # Add titles and labels
        ax.set_title("Comparison of Steps Taken by Sorting Algorithms", fontsize=16)
        ax.set_xlabel("Input Size", fontsize=14)
        ax.set_ylabel("Steps Taken", fontsize=14)
        ax.legend(fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)

        # Embed the Matplotlib figure into the Tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()

if __name__ == "__main__":
    # Example data
    input_sizes1 = [10, 20, 30, 40, 50]
    steps_taken1 = [15, 60, 135, 240, 375]

    input_sizes2 = [10, 20, 30, 40, 50]
    steps_taken2 = [20, 80, 180, 320, 500]

    root = tk.Tk()
    GraphPlaceholderApp(root, input_sizes1, steps_taken1, input_sizes2, steps_taken2,
                        label1="Algorithm 1", label2="Algorithm 2")
    root.mainloop()
