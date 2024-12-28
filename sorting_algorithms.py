import time

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.main_writes = 0
        self.aux_writes = 0
        self.time_taken = 0.0
        self.totsteps=0

    def get_total_steps(self):
        self.totsteps = self.comparisons + self.swaps + self.main_writes + self.aux_writes
        return (self.totsteps)
    def reset(self):
        self.comparisons = 0
        self.swaps = 0
        self.main_writes = 0
        self.aux_writes = 0
        self.time_taken = 0.0
        self.totsteps = 0

class SortingAlgorithms:
    """
    A class that implements various sorting algorithms.
    """
    metrics = Metrics()

    @staticmethod
    def measure_time(func):
        def wrapper(arr, metrics):
            start_time = time.time()
            result = func(arr, metrics)
            metrics.time_taken = time.time() - start_time
            return result
        return wrapper



    @staticmethod
    @measure_time
    def quick_sort(arr, metrics):
        def partition(low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                metrics.comparisons += 1  # Increment comparison count
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    metrics.swaps += 1  # Increment swap count
                    metrics.main_writes += 2  # Increment write count
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            metrics.swaps += 1  # Increment swap count
            metrics.main_writes += 2  # Increment write count
            return i + 1

        def quick_sort_recursive(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_recursive(low, pi - 1)
                quick_sort_recursive(pi + 1, high)

        quick_sort_recursive(0, len(arr) - 1)

    @staticmethod
    @measure_time
    def merge_sort(arr, metrics):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            metrics.aux_writes += len(left) + len(right)  # Counting auxiliary writes for splits

            SortingAlgorithms.merge_sort(left, metrics)
            SortingAlgorithms.merge_sort(right, metrics)

            i = j = k = 0

            while i < len(left) and j < len(right):
                metrics.comparisons += 1  # Increment comparison count
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
                metrics.main_writes += 1  # Increment main writes

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                metrics.main_writes += 1  # Increment main writes

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                metrics.main_writes += 1  # Increment main writes

    @staticmethod
    @measure_time
    def shell_sort(arr, metrics):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                metrics.aux_writes += 1  # Counting auxiliary writes

                j = i
                while j >= gap and arr[j - gap] > temp:
                    metrics.comparisons += 1  # Increment comparisons
                    arr[j] = arr[j - gap]
                    metrics.main_writes += 1  # Increment main writes
                    j -= gap

                arr[j] = temp
                metrics.main_writes += 1  # Increment main writes
            gap //= 2


    @staticmethod
    @measure_time
    def selection_sort(arr, metrics):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                metrics.comparisons += 1  # Increment comparisons
                if arr[j] < arr[min_idx]:
                    min_idx = j

            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                metrics.swaps += 1  # Increment swaps
                metrics.main_writes += 2  # Increment main writes for the swap

    @staticmethod
    @measure_time
    def insertion_sort(arr, metrics):
        for i in range(1, len(arr)):
            key = arr[i]
            metrics.aux_writes += 1  # Increment auxiliary writes
            j = i - 1

            while j >= 0 and key < arr[j]:
                metrics.comparisons += 1  # Increment comparisons
                arr[j + 1] = arr[j]
                metrics.main_writes += 1  # Increment main writes
                j -= 1

            arr[j + 1] = key
            metrics.main_writes += 1  # Increment main writes for placement


    @staticmethod
    @measure_time
    def heap_sort(arr, metrics):
        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n:
                metrics.comparisons += 1  # Increment comparisons
                if arr[l] > arr[largest]:
                    largest = l

            if r < n:
                metrics.comparisons += 1  # Increment comparisons
                if arr[r] > arr[largest]:
                    largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                metrics.swaps += 1  # Increment swaps
                metrics.main_writes += 2  # Increment main writes
                heapify(n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            metrics.swaps += 1  # Increment swaps
            metrics.main_writes += 2  # Increment main writes
            heapify(i, 0)


    @staticmethod
    @measure_time
    def gravity_sort(arr, metrics):
        max_val = max(arr)
        metrics.comparisons += len(arr)  # Comparisons to find max

        beads = [0] * (len(arr) * max_val)
        metrics.aux_writes += len(beads)  # Auxiliary writes for bead array initialization

        for i, num in enumerate(arr):
            for j in range(num):
                beads[i * max_val + j] = 1
                metrics.aux_writes += 1  # Increment auxiliary writes for setting beads

        for j in range(max_val):
            sum_ = 0
            for i in range(len(arr)):
                sum_ += beads[i * max_val + j]
                beads[i * max_val + j] = 0
                metrics.aux_writes += 1  # Auxiliary writes for resetting beads

            for i in range(len(arr) - 1, len(arr) - sum_ - 1, -1):
                beads[i * max_val + j] = 1
                metrics.aux_writes += 1  # Auxiliary writes for setting beads

        for i in range(len(arr)):
            arr[i] = sum(beads[i * max_val:(i + 1) * max_val])
            metrics.main_writes += 1  # Main writes for updating the array



    @staticmethod
    @measure_time
    def radix_sort(arr, metrics):
        def counting_sort(exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                metrics.comparisons += 1  # Comparisons during counting
                index = (arr[i] // exp) % 10
                count[index] += 1
                metrics.aux_writes += 1  # Auxiliary writes for count array

            for i in range(1, 10):
                metrics.comparisons += 1  # Comparisons during cumulative count
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                metrics.comparisons += 1  # Comparisons during output array construction
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                metrics.aux_writes += 1  # Auxiliary writes for output array
                count[index] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]
                metrics.main_writes += 1  # Main writes for updating the original array

        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            counting_sort(exp)
            exp *= 10


    @staticmethod
    @measure_time
    def gnome_sort(arr, metrics):
        index = 0
        while index < len(arr):
            if index == 0 or arr[index] >= arr[index - 1]:
                metrics.comparisons += 1  # Increment comparisons
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                metrics.swaps += 1  # Increment swaps
                index -= 1


    @staticmethod
    @measure_time
    def odd_even_sort(arr, metrics):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(arr) - 1, 2):  # Odd indexed passes
                metrics.comparisons += 1  # Increment comparisons
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1  # Increment swaps
                    is_sorted = False

            for i in range(0, len(arr) - 1, 2):  # Even indexed passes
                metrics.comparisons += 1  # Increment comparisons
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1  # Increment swaps
                    is_sorted = False


    @staticmethod
    @measure_time
    def bubble_sort(arr, metrics):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                metrics.comparisons += 1  # Increment comparisons
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    metrics.swaps += 1  # Increment swaps


    @staticmethod
    @measure_time
    def cocktail_shaker_sort(arr, metrics):
        n = len(arr)
        start = 0
        end = n - 1
        swapped = True
        while swapped:
            swapped = False
            for i in range(start, end):  # Forward pass
                metrics.comparisons += 1  # Increment comparisons
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1  # Increment swaps
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):  # Backward pass
                metrics.comparisons += 1  # Increment comparisons
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1  # Increment swaps
                    swapped = True

            start += 1


    @staticmethod
    @measure_time
    def counting_sort(arr, metrics):
        max_val = max(arr)
        min_val = min(arr)
        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements
        output = [0] * len(arr)

        for i in arr:  # Count occurrences
            count[i - min_val] += 1
            metrics.aux_writes += 1  # Increment auxiliary writes

        for i in range(1, len(count)):  # Cumulative count
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):  # Place elements in output
            output[count[arr[i] - min_val] - 1] = arr[i]
            metrics.aux_writes += 1  # Increment auxiliary writes
            count[arr[i] - min_val] -= 1

        for i in range(len(arr)):  # Copy back to the original array
            arr[i] = output[i]
            metrics.main_writes += 1  # Increment main writes


    @staticmethod
    @measure_time
    def bucket_sort(arr, metrics):
        if len(arr) == 0:
            return

        bucket_count = len(arr)
        max_val = max(arr)
        buckets = [[] for _ in range(bucket_count)]

        for i in arr:  # Distribute elements into buckets
            index = int(i / max_val * (bucket_count - 1))
            buckets[index].append(i)
            metrics.aux_writes += 1  # Increment auxiliary writes for bucket population

        for bucket in buckets:  # Sort individual buckets
            SortingAlgorithms.insertion_sort(bucket, metrics)

        k = 0
        for bucket in buckets:  # Concatenate buckets back to the array
            for val in bucket:
                arr[k] = val
                metrics.main_writes += 1  # Increment main writes
                k += 1

