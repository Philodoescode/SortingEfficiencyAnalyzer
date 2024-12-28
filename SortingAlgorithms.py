import time

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.main_writes = 0
        self.aux_writes = 0
        self.time_taken = 0.0

    def reset(self):
        self.comparisons = 0
        self.swaps = 0
        self.main_writes = 0
        self.aux_writes = 0
        self.time_taken = 0.0

class SortingAlgorithms:
    """
    A class that implements various sorting algorithms.
    """
    metrics = Metrics()

    @staticmethod
    def measure_time(func):
        def wrapper(arr):
            start_time = time.time()
            func(arr)
            SortingAlgorithms.metrics.time_taken = time.time() - start_time
        return wrapper

    @staticmethod
    @measure_time
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            SortingAlgorithms.metrics.aux_writes += len(left) + len(right)  

            SortingAlgorithms.merge_sort(left)
            SortingAlgorithms.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                SortingAlgorithms.metrics.comparisons += 1  
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
                SortingAlgorithms.metrics.main_writes += 1  

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                SortingAlgorithms.metrics.main_writes += 1  

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                SortingAlgorithms.metrics.main_writes += 1  

    @staticmethod
    @measure_time
    def shell_sort(arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                SortingAlgorithms.metrics.aux_writes += 1  

                j = i
                while j >= gap and arr[j - gap] > temp:
                    SortingAlgorithms.metrics.comparisons += 1  
                    arr[j] = arr[j - gap]
                    SortingAlgorithms.metrics.main_writes += 1  
                    j -= gap

                arr[j] = temp
                SortingAlgorithms.metrics.main_writes += 1  
            gap //= 2

    @staticmethod
    @measure_time
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                SortingAlgorithms.metrics.comparisons += 1  
                if arr[j] < arr[min_idx]:
                    min_idx = j

            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                SortingAlgorithms.metrics.swaps += 1  
                SortingAlgorithms.metrics.main_writes += 2  

    @staticmethod
    @measure_time
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            SortingAlgorithms.metrics.aux_writes += 1  
            j = i - 1

            while j >= 0 and key < arr[j]:
                SortingAlgorithms.metrics.comparisons += 1  
                arr[j + 1] = arr[j]
                SortingAlgorithms.metrics.main_writes += 1  
                j -= 1

            arr[j + 1] = key
            SortingAlgorithms.metrics.main_writes += 1  

    @staticmethod
    @measure_time
    def heap_sort(arr):
        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n:
                SortingAlgorithms.metrics.comparisons += 1  
                if arr[l] > arr[largest]:
                    largest = l

            if r < n:
                SortingAlgorithms.metrics.comparisons += 1  
                if arr[r] > arr[largest]:
                    largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                SortingAlgorithms.metrics.swaps += 1  
                SortingAlgorithms.metrics.main_writes += 2  
                heapify(n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            SortingAlgorithms.metrics.swaps += 1  
            SortingAlgorithms.metrics.main_writes += 2  
            heapify(i, 0)

    @staticmethod
    @measure_time
    def gravity_sort(arr):
        max_val = max(arr)
        SortingAlgorithms.metrics.comparisons += len(arr)  

        beads = [0] * (len(arr) * max_val)
        SortingAlgorithms.metrics.aux_writes += len(beads)  

        for i, num in enumerate(arr):
            for j in range(num):
                beads[i * max_val + j] = 1
                SortingAlgorithms.metrics.aux_writes += 1  

        for j in range(max_val):
            sum_ = 0
            for i in range(len(arr)):
                sum_ += beads[i * max_val + j]
                beads[i * max_val + j] = 0
                SortingAlgorithms.metrics.aux_writes += 1  

            for i in range(len(arr) - 1, len(arr) - sum_ - 1, -1):
                beads[i * max_val + j] = 1
                SortingAlgorithms.metrics.aux_writes += 1  

        for i in range(len(arr)):
            arr[i] = sum(beads[i * max_val:(i + 1) * max_val])
            SortingAlgorithms.metrics.main_writes += 1  


    @staticmethod
    @measure_time
    def radix_sort(arr, metrics):
        def counting_sort(exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                metrics.comparisons += 1
                index = (arr[i] // exp) % 10
                count[index] += 1
                metrics.aux_writes += 1

            for i in range(1, 10):
                metrics.comparisons += 1
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                metrics.comparisons += 1
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                metrics.aux_writes += 1
                count[index] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]
                metrics.main_writes += 1

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
                metrics.comparisons += 1
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                metrics.swaps += 1
                index -= 1

    @staticmethod
    @measure_time
    def odd_even_sort(arr, metrics):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(arr) - 1, 2):
                metrics.comparisons += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1
                    is_sorted = False

            for i in range(0, len(arr) - 1, 2):
                metrics.comparisons += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1
                    is_sorted = False

    @staticmethod
    @measure_time
    def bubble_sort(arr, metrics):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                metrics.comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    metrics.swaps += 1

    @staticmethod
    @measure_time
    def cocktail_shaker_sort(arr, metrics):
        n = len(arr)
        start = 0
        end = n - 1
        swapped = True
        while swapped:
            swapped = False
            for i in range(start, end):
                metrics.comparisons += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                metrics.comparisons += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    metrics.swaps += 1
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

        for i in arr:
            count[i - min_val] += 1
            metrics.aux_writes += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            metrics.aux_writes += 1
            count[arr[i] - min_val] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]
            metrics.main_writes += 1

    @staticmethod
    @measure_time
    def bucket_sort(arr, metrics):
        if len(arr) == 0:
            return

        bucket_count = len(arr)
        max_val = max(arr)
        buckets = [[] for _ in range(bucket_count)]

        for i in arr:
            index = int(i / max_val * (bucket_count - 1))
            buckets[index].append(i)
            metrics.aux_writes += 1

        for bucket in buckets:
            SortingAlgorithms.insertion_sort(bucket, metrics)

        k = 0
        for bucket in buckets:
            for val in bucket:
                arr[k] = val
                metrics.main_writes += 1
                k += 1
