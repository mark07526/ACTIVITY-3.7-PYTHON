# ==================================================
# ASSESSMENT 3.7: Sorting Algorithms - Merge Sort
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


# Step 2: Merge Sort (Divide and Conquer)
# Divide: split the array in half
# Conquer: sort each half recursively
# Combine: merge the two sorted halves
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


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


if __name__ == "__main__":
    unsorted_array = build_unsorted_array(full_name)
    sorted_array = merge_sort(unsorted_array)

    print("--- ASSESSMENT 3.7: Merge Sort ---")
    print("Full Name      :", full_name)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)