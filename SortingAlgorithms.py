class SortingAlgorithms:
    """
    A class that implements various sorting algorithms.
    """

    @staticmethod
    def quick_sort(arr):
        def partition(low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quicksort_recursive(low, high):
            if low < high:
                pi = partition(low, high)
                quicksort_recursive(low, pi - 1)
                quicksort_recursive(pi + 1, high)

        quicksort_recursive(0, len(arr) - 1)

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            SortingAlgorithms.merge_sort(left)
            SortingAlgorithms.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    @staticmethod
    def shell_sort(arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def heap_sort(arr):
        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l

            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(i, 0)

    @staticmethod
    def gravity_sort(arr):
        max_val = max(arr)
        beads = [0] * (len(arr) * max_val)

        for i, num in enumerate(arr):
            for j in range(num):
                beads[i * max_val + j] = 1

        for j in range(max_val):
            sum_ = 0
            for i in range(len(arr)):
                sum_ += beads[i * max_val + j]
                beads[i * max_val + j] = 0

            for i in range(len(arr) - 1, len(arr) - sum_ - 1, -1):
                beads[i * max_val + j] = 1

        for i in range(len(arr)):
            arr[i] = sum(beads[i * max_val:(i + 1) * max_val])

    @staticmethod
    def radix_sort(arr):
        def counting_sort(exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = (arr[i] // exp) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]

        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            counting_sort(exp)
            exp *= 10

    @staticmethod
    def gnome_sort(arr):
        index = 0
        while index < len(arr):
            if index == 0 or arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1

    @staticmethod
    def odd_even_sort(arr):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(arr) - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False

            for i in range(0, len(arr) - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def cocktail_shaker_sort(arr):
        n = len(arr)
        start = 0
        end = n - 1
        swapped = True
        while swapped:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1

    @staticmethod
    def counting_sort(arr):
        max_val = max(arr)
        min_val = min(arr)
        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements
        output = [0] * len(arr)

        for i in arr:
            count[i - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    @staticmethod
    def bucket_sort(arr):
        if len(arr) == 0:
            return

        bucket_count = len(arr)
        max_val = max(arr)
        buckets = [[] for _ in range(bucket_count)]

        for i in arr:
            index = int(i / max_val * (bucket_count - 1))
            buckets[index].append(i)

        for bucket in buckets:
            SortingAlgorithms.insertion_sort(bucket)

        k = 0
        for bucket in buckets:
            for val in bucket:
                arr[k] = val
                k += 1
