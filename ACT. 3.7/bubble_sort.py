# ==================================================
# ASSESSMENT 3.7: Sorting Algorithms - Bubble Sort
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


# Step 2: Bubble Sort
# Repeatedly compare adjacent elements and swap them if they are in the wrong order
def bubble_sort(arr):
    result = arr.copy()              # keep the unsorted array unchanged
    n = len(result)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:              # no swaps means it is already sorted
            break

    return result


if __name__ == "__main__":
    unsorted_array = build_unsorted_array(full_name)
    sorted_array = bubble_sort(unsorted_array)

    print("--- ASSESSMENT 3.7: Bubble Sort ---")
    print("Full Name      :", full_name)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)