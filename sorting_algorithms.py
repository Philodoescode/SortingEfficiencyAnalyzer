import time


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
    @staticmethod
    def gnome_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        index = 0
        while index < len(arr):
            SortingAlgorithms.step_counter += 1  # For each loop iteration
            if index == 0 or arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                SortingAlgorithms.step_counter += 3  # For swap
                index -= 1

    @staticmethod
    def odd_even_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(arr) - 1, 2):
                SortingAlgorithms.step_counter += 1  # For each comparison
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    SortingAlgorithms.step_counter += 3  # For swap
                    is_sorted = False

            for i in range(0, len(arr) - 1, 2):
                SortingAlgorithms.step_counter += 1  # For each comparison
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    SortingAlgorithms.step_counter += 3  # For swap
                    is_sorted = False

    @staticmethod
    def bubble_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                SortingAlgorithms.step_counter += 1  # For each comparison
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    SortingAlgorithms.step_counter += 3  # For swap

    @staticmethod
    def cocktail_shaker_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        n = len(arr)
        start = 0
        end = n - 1
        swapped = True
        while swapped:
            swapped = False
            for i in range(start, end):
                SortingAlgorithms.step_counter += 1  # For each comparison
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    SortingAlgorithms.step_counter += 3  # For swap
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                SortingAlgorithms.step_counter += 1  # For each comparison
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    SortingAlgorithms.step_counter += 3  # For swap
                    swapped = True

            start += 1

    @staticmethod
    def counting_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        max_val = max(arr)
        min_val = min(arr)
        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements
        output = [0] * len(arr)

        for i in arr:
            count[i - min_val] += 1
            SortingAlgorithms.step_counter += 1  # For counting

        for i in range(1, len(count)):
            count[i] += count[i - 1]
            SortingAlgorithms.step_counter += 1  # For cumulative sum

        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
            SortingAlgorithms.step_counter += 2  # For placement

        for i in range(len(arr)):
            arr[i] = output[i]
            SortingAlgorithms.step_counter += 1  # For copying to original array

    @staticmethod
    def bucket_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter
        if len(arr) == 0:
            return

        bucket_count = len(arr)
        max_val = max(arr)
        buckets = [[] for _ in range(bucket_count)]

        for i in arr:
            index = int(i / max_val * (bucket_count - 1))
            buckets[index].append(i)
            SortingAlgorithms.step_counter += 1  # For bucket assignment

        k = 0
        for bucket in buckets:
            bucket.sort()  # Using Python's built-in sort for simplicity
            for val in bucket:
                arr[k] = val
                k += 1
                SortingAlgorithms.step_counter += 1  # For placement

    @staticmethod
    def radix_sort(arr):
        SortingAlgorithms.step_counter = 0  # Reset counter

        def counting_sort(exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = (arr[i] // exp) % 10
                count[index] += 1
                SortingAlgorithms.step_counter += 1  # For counting

            for i in range(1, 10):
                count[i] += count[i - 1]
                SortingAlgorithms.step_counter += 1  # For cumulative sum

            i = n - 1
            while i >= 0:
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1
                SortingAlgorithms.step_counter += 2  # For placement
                i -= 1

            for i in range(n):
                arr[i] = output[i]
                SortingAlgorithms.step_counter += 1  # For copying to original array

        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            counting_sort(exp)
            exp *= 10

    @staticmethod
    def gravity_sort(arr):  # Bead Sort
        SortingAlgorithms.step_counter = 0  # Reset counter
        max_val = max(arr)
        beads = [0] * (len(arr) * max_val)

        for i, num in enumerate(arr):
            for j in range(num):
                beads[i * max_val + j] = 1
                SortingAlgorithms.step_counter += 1  # For placing beads

        for j in range(max_val):
            sum_ = 0
            for i in range(len(arr)):
                sum_ += beads[i * max_val + j]
                beads[i * max_val + j] = 0
                SortingAlgorithms.step_counter += 1  # For gravity simulation

            for i in range(len(arr) - 1, len(arr) - sum_ - 1, -1):
                beads[i * max_val + j] = 1
                SortingAlgorithms.step_counter += 1  # For bead placement

        for i in range(len(arr)):
            arr[i] = sum(beads[i * max_val:(i + 1) * max_val])
            SortingAlgorithms.step_counter += 1  # For copying to original array


import math

class AsymptoticNotations:
    """
    A class to calculate and return the asymptotic notations for different sorting algorithms.
    """

    @staticmethod
    def insertion_sort(n):
        # Time complexity: O(n^2)
        return n ** 2

    @staticmethod
    def selection_sort(n):
        # Time complexity: O(n^2)
        return n ** 2

    @staticmethod
    def bubble_sort(n):
        # Time complexity: O(n^2)
        return n ** 2

    @staticmethod
    def cocktail_shaker_sort(n):
        # Time complexity: O(n^2)
        return n ** 2

    @staticmethod
    def gnome_sort(n):
        # Time complexity: O(n^2)
        return n ** 2

    @staticmethod
    def odd_even_sort(n):
        # Time complexity: O(n^2)
        return n ** 2

    @staticmethod
    def quick_sort(n):
        # Average case: O(n log n), Worst case: O(n^2)
        return n * math.log2(n)

    @staticmethod
    def merge_sort(n):
        # Time complexity: O(n log n)
        return n * math.log2(n)

    @staticmethod
    def heap_sort(n):
        # Time complexity: O(n log n)
        return n * math.log2(n)

    @staticmethod
    def shell_sort(n):
        # Time complexity: Depends on gap sequence, average case is O(n^(3/2)) for common sequences.
        return n ** (3/2)

    @staticmethod
    def counting_sort(n):
        # Time complexity: O(n + k), where k is the range of input values. Assuming k = n for simplicity.
        return n + n

    @staticmethod
    def bucket_sort(n):
        # Time complexity: O(n + k), assuming k = n for simplicity.
        return n + n

    @staticmethod
    def radix_sort(n):
        # Time complexity: O(d * (n + b)), where d is the number of digits and b is the base. Assuming b = 10 and d = log10(n).
        d = math.log10(n)  # Number of digits
        return d * (n + 10)

    @staticmethod
    def gravity_sort(n):
        # Time complexity: O(n * max_value). Assuming max_value = n for simplicity.
        return n * n

# Example usage:
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6,5,5,5,5,5,5,8,8,8,8,8,8,8,15,47,5,1,3,78,100,58]
    start_time = time.time_ns()
    SortingAlgorithms.insertion_sort(arr)
    end_time = time.time_ns()
    print("Sorted array:", arr)
    print("Steps taken:", end_time - start_time)