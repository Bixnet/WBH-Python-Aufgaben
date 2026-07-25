import operator


def bubble_sort(lst, op=operator.gt, key=lambda x: x):
    n = len(lst)

    for i in range(n - 1):
        swapped = False

        for j in range(0, n - i - 1):
            if op(key(lst[j]), key(lst[j + 1])):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break


# Beispielaufrufe

lst1 = [3, 2, 1]
bubble_sort(lst1)
print(lst1)  # [1, 2, 3]

lst2 = [1, 2, 3]
bubble_sort(lst2, op=operator.lt)
print(lst2)  # [3, 2, 1]

lst3 = ['Start', 'see', 'computer', 'ast', 'Baum']
bubble_sort(lst3, key=str.lower)
print(lst3)