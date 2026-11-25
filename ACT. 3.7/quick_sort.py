# ==================================================
# ASSESSMENT 3.7: Sorting Algorithms - Quick Sort
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


# Step 2: Quick Sort (Divide and Conquer)
# Divide: choose a pivot and partition the array around it
# Conquer: sort the left and right parts recursively
# Combine: left + pivot + right
def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[-1]                      # last element is the pivot
    smaller = []
    larger = []

    for item in arr[:-1]:
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


if __name__ == "__main__":
    unsorted_array = build_unsorted_array(full_name)
    sorted_array = quick_sort(unsorted_array)

    print("--- ASSESSMENT 3.7: Quick Sort ---")
    print("Full Name      :", full_name)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)