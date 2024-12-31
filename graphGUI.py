import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Frame

class GraphPlaceholderApp:
    def __init__(self, master, x1, y1, x2, y2, x3=None, y3=None, label1=None, label2=None, label3=None, graph_title="Graph", type= None):
        self.master = master
        self.master.title("Graph Display")
        self.master.configure(bg="#87CEEB")  # Sky blue

        # Configure the window size
        self.master.geometry("800x600")

        # Create the main frame for the graph
        self.graph_frame = Frame(self.master, bg="#87CEEB")
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add the graph
        self.create_graph(x1, y1, x2, y2, x3, y3, label1, label2, label3, graph_title)

    def create_graph(self, x1, y1, x2, y2, x3, y3, label1, label2, label3, graph_title):
        # Create a Matplotlib figure and axis
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)


        # Plot the data
        ax.plot(x1, y1, label=label1, marker='o', linestyle='-')
        if type is not None:
            ax.plot(x2, y2, label=label2, marker='s', linestyle='--')
        else:
            ax.plot(x3, y3, label=label3, marker='o', linestyle='-')
        if x3 is not None and y3 is not None:
            ax.plot(x3, y3, label=label3, marker='^', linestyle=':')

        # Add titles and labels
        ax.set_title(graph_title, fontsize=16)
        ax.set_xlabel("Input Size", fontsize=14)
        ax.set_ylabel("Steps Taken" if "Steps" in graph_title else "Time Taken", fontsize=14)
        ax.legend(fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)

        # Embed the Matplotlib figure into the Tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()


    import numpy as np





def plot_steps_comparison(x1, y1, x2, y2, x3, y3, label1, label2, label3, type):
    plt.figure(figsize=(10, 6))

    # Plot the first dataset
    plt.plot(x1, y1, label=label1, marker='o')

    # Plot the second dataset
    plt.plot(x2, y2, label=label2, marker='s')

    # Plot the third dataset
    if x3 and y3:
        plt.plot(x3, y3, label=label3, marker='^')

    # Add titles and labels
    plt.title(f"Comparison of {type} Taken by Sorting Algorithms", fontsize=16)
    plt.xlabel("Input Size", fontsize=14)
    plt.ylabel(f"{type} Taken", fontsize=14)

    # Add legend and grid
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("comparison.png")
    print(f"Graph saved to comparison.png")

def plot_asymptotic_comparison(x1, y1, x2, y2, x3, y3, label1, label2, label3, type):
    plt.figure(figsize=(10, 6))

    # Plot the first dataset
    plt.plot(x1, y1, label=label1, marker='o')

    # Plot the second dataset
    plt.plot(x2, y2, label=label2, marker='s')

    # Plot the third dataset
    plt.plot(x3, y3, label=label3, marker='^')

    # Add titles and labels
    plt.title(f"Comparison of {type} Taken by Sorting Algorithms", fontsize=16)
    plt.xlabel("Input Size", fontsize=14)
    plt.ylabel(f"{type} Taken", fontsize=14)

    # Add legend and grid
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("asymptotic.png")
    print(f"Graph saved to asymptotic.png")

if __name__ == "__main__":
    # Example data for testing
    x1 = [10, 20, 30, 40, 50]
    y1 = [15, 60, 135, 240, 375]
    x2 = [10, 20, 30, 40, 50]
    y2 = [20, 80, 180, 320, 500]
    x3 = [10, 20, 30, 40, 50]
    y3 = [10, 40, 90, 160, 250]

    root = tk.Tk()
    app = GraphPlaceholderApp(root, x1, y1, x2, y2, x3, y3, "Algorithm 1", "Algorithm 2", "Best Case", "Comparison of Steps Taken")
    root.mainloop()
