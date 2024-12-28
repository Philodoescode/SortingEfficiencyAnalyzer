class SortingAlgorithms:
    """
    A class that implements various sorting algorithms.
    """

    step_counter = 0  # Class-level attribute to track steps

    @staticmethod
    def quick_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter

        def partition(low, high):
            pivot = arr[high]
            SortingAlgorithms.step_counter += 1  # For pivot assignment
            i = low - 1
            for j in range(low, high):
                SortingAlgorithms.step_counter += 1  # For each comparison
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    SortingAlgorithms.step_counter += 3  # For swap
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            SortingAlgorithms.step_counter += 3  # For swap
            return i + 1

        def quicksort_recursive(low, high):
            if low < high:
                SortingAlgorithms.step_counter += 1  # For comparison
                pi = partition(low, high)
                quicksort_recursive(low, pi - 1)
                quicksort_recursive(pi + 1, high)

        quicksort_recursive(0, len(arr) - 1)

    @staticmethod
    def merge_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter

        def merge_sort_recursive(arr):
            if len(arr) > 1:
                SortingAlgorithms.step_counter += 1  # For comparison
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                SortingAlgorithms.step_counter += len(arr)  # For splitting
                merge_sort_recursive(left)
                merge_sort_recursive(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    SortingAlgorithms.step_counter += 1  # For comparison
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                    SortingAlgorithms.step_counter += 1  # For assignment

                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                    SortingAlgorithms.step_counter += 1  # For assignment

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                    SortingAlgorithms.step_counter += 1  # For assignment

        merge_sort_recursive(arr)

    @staticmethod
    def shell_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                SortingAlgorithms.step_counter += 1  # For assignment
                j = i
                while j >= gap and arr[j - gap] > temp:
                    SortingAlgorithms.step_counter += 2  # For comparison and assignment
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
                SortingAlgorithms.step_counter += 1  # For assignment
            gap //= 2

    @staticmethod
    def selection_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                SortingAlgorithms.step_counter += 1  # For comparison
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            SortingAlgorithms.step_counter += 3  # For swap

    @staticmethod
    def insertion_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        for i in range(1, len(arr)):
            key = arr[i]
            SortingAlgorithms.step_counter += 1  # For assignment
            j = i - 1
            while j >= 0 and key < arr[j]:
                SortingAlgorithms.step_counter += 2  # For comparison and assignment
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            SortingAlgorithms.step_counter += 1  # For assignment

    @staticmethod
    def heap_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter

        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            SortingAlgorithms.step_counter += 2  # For assignments
            if l < n and arr[l] > arr[largest]:
                largest = l
                SortingAlgorithms.step_counter += 1  # For comparison

            if r < n and arr[r] > arr[largest]:
                largest = r
                SortingAlgorithms.step_counter += 1  # For comparison

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                SortingAlgorithms.step_counter += 3  # For swap
                heapify(n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            SortingAlgorithms.step_counter += 3  # For swap
            heapify(i, 0)

    # Add similar counter logic to remaining algorithms as needed.

# Example usage:
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    SortingAlgorithms.insertion_sort(arr)
    print("Sorted array:", arr)
    print("Steps taken:", SortingAlgorithms.step_counter)
