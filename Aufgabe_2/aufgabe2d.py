import time
import random


def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break


def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    smaller = []
    equal = []
    larger = []
    for element in lst:
        if element < pivot:
            smaller.append(element)
        elif element > pivot:
            larger.append(element)
        else:
            equal.append(element)
    return quick_sort(smaller) + equal + quick_sort(larger)


def merge(lst1, lst2):
    result = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)


# --- Zeitmessung ---

sizes = [1000, 10000, 100000]

for n in sizes:
    numbers = [random.random() for _ in range(n)]
    print(f"n = {n}")

    # Quick Sort
    start = time.time()
    quick_sort(numbers.copy())
    end = time.time()
    print(f"quick: {end - start:.5f} Sekunden")

    # Merge Sort
    start = time.time()
    merge_sort(numbers.copy())
    end = time.time()
    print(f"merge: {end - start:.5f} Sekunden")

    # Bubble Sort (in place, deshalb Kopie nötig!)
    bubble_input = numbers.copy()
    start = time.time()
    bubble_sort(bubble_input)
    end = time.time()
    print(f"bubble: {end - start:.5f} Sekunden")

    print()


