import matplotlib.pyplot as plt

def plot_steps_comparison(x1, y1, x2, y2, label1, label2):

    plt.figure(figsize=(10, 6))

    # Plot the first dataset
    plt.plot(x1, y1, label=label1, marker='o')

    # Plot the second dataset
    plt.plot(x2, y2, label=label2, marker='s')

    # Add titles and labels
    plt.title("Comparison of Steps Taken by Sorting Algorithms", fontsize=16)
    plt.xlabel("Input Size", fontsize=14)
    plt.ylabel("Steps Taken", fontsize=14)

    # Add legend and grid
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("comparison.png")
    print(f"Graph saved to comparison.png")

# Example usage
if __name__ == "__main__":
    # Example data
    input_sizes1 = [10, 20, 30, 40, 50]
    steps_taken1 = [15, 60, 135, 240, 375]

    input_sizes2 = [10, 20, 30, 40, 50]
    steps_taken2 = [20, 80, 180, 320, 500]

    plot_steps_comparison(input_sizes1, steps_taken1, input_sizes2, steps_taken2,
                          label1="Algorithm 1", label2="Algorithm 2")
