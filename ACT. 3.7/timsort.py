# ==================================================
# ASSESSMENT 3.7: Sorting Algorithms - Timsort
# ==================================================

full_name = "Mark Vengie Gomera"


# Step 1: Build the unsorted array from the full name
# - only letters are kept (spaces and symbols are excluded)
# - duplicate letters are discarded (each letter appears once)
def build_unsorted_array(name):
    letters = []
    for ch in name.upper():
        if ch.isalpha() and ch not in letters:
            letters.append(ch)
    return letters


# Step 2: Timsort (hybrid of Insertion Sort and Merge Sort)
# 1. Split the array into small runs
# 2. Sort every run using Insertion Sort
# 3. Merge the sorted runs using Merge Sort's merge step
RUN_SIZE = 4


def insertion_sort_run(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def timsort(arr):
    result = arr.copy()
    n = len(result)

    # sort each run with Insertion Sort
    for start in range(0, n, RUN_SIZE):
        end = min(start + RUN_SIZE - 1, n - 1)
        insertion_sort_run(result, start, end)

    # merge the runs, doubling the merge size each time
    size = RUN_SIZE
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(start + size, n)
            end = min(start + 2 * size, n)
            result[start:end] = merge(result[start:mid], result[mid:end])
        size *= 2

    return result


if __name__ == "__main__":
    unsorted_array = build_unsorted_array(full_name)
    sorted_array = timsort(unsorted_array)

    print("--- ASSESSMENT 3.7: Timsort ---")
    print("Full Name      :", full_name)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)