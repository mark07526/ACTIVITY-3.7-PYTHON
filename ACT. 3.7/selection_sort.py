# ==================================================
# ASSESSMENT 3.7: Sorting Algorithms - Selection Sort
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


# Step 2: Selection Sort
# Repeatedly find the smallest element in the unsorted part
# and place it at the front of that part
def selection_sort(arr):
    result = arr.copy()
    n = len(result)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]

    return result


if __name__ == "__main__":
    unsorted_array = build_unsorted_array(full_name)
    sorted_array = selection_sort(unsorted_array)

    print("--- ASSESSMENT 3.7: Selection Sort ---")
    print("Full Name      :", full_name)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)