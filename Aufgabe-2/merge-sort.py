# merge-sort -> Divide and conquer

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
    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


# Beispielaufrufe
lst1 = [1, 3, 5]
lst2 = [2, 4, 7, 9]
merged = merge(lst1, lst2)
print(merged)  # [1, 2, 3, 4, 5, 7, 9]

lst = [2, 3, 6, 1, 4, 7, 5, 9, 8]
sorted_lst = merge_sort(lst)

print(sorted_lst)  # sorted
print(lst)  # unsorted
