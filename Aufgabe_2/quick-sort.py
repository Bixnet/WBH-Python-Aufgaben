# Quck-sort -> Divide and conquer

def quick_sort(lst):
    # Basisfall: 0 oder 1 Element ist bereits sortiert
    if len(lst) < 2:
        return lst

    # Pivot-Element: das erste Element der Liste
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

    # Rekursion auf beiden Teillisten, dann kombinieren
    return quick_sort(smaller) + equal + quick_sort(larger)


# Beispielaufruf
lst = [2, 3, 6, 1, 4, 7, 5, 9, 8]
sorted_lst = quick_sort(lst)
print(f"verändert: {sorted_lst}")  
print(f"unverändert:  {lst}")
