import graphDesigner
import SortingAlgorithms
import random
sizes1 =[]
steps1 =[]

sizes2 =[]
steps2 =[]
for i in range(5, 1001, 5):
    sizes1.append(i)
    # Generate a randomly sorted array of size i
    random_array = random.sample(range(1, i + 1), i)

    # Reset step counter for each sorting operation
    SortingAlgorithms.SortingAlgorithms.step_counter = 0

    # Perform sorting
    SortingAlgorithms.SortingAlgorithms.heap_sort(random_array)
    steps1.append(SortingAlgorithms.SortingAlgorithms.step_counter)
for i in range(5, 1001, 5):
    sizes2.append(i)
    # Generate a randomly sorted array of size i
    random_array = random.sample(range(1, i + 1), i)

    # Reset step counter for each sorting operation
    SortingAlgorithms.SortingAlgorithms.step_counter = 0

    # Perform sorting
    SortingAlgorithms.SortingAlgorithms.insertion_sort(random_array)
    steps2.append(SortingAlgorithms.SortingAlgorithms.step_counter)

graphDesigner.plot_steps_comparison(sizes1, steps1,sizes2, steps2, "heap sort", "insertion sort")