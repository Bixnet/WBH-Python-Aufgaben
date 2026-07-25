import random


def bubble_sort(lst):
    n = len(lst)

    # Äußere Schleife: von Index 0 bis zum vorletzten gültigen Index
    for i in range(n - 1):
        swapped = False

        # Innere Schleife: über alle noch nicht sortierten Elemente
        for j in range(0, n - i - 1):

            # Vorgänger und Nachfolger vergleichen
            if lst[j] > lst[j + 1]:

                # Vertauschen, wenn Reihenfolge falsch ist
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        # Vorzeitiger Abbruch, wenn in diesem Durchlauf nichts getauscht wurde
        if not swapped:
            break


# Beispielaufrufe

lst = [2, 3, 6, 1, 4, 7, 5, 9, 8]
bubble_sort(lst)
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [random.random() for _ in range(10)]  # 10 Zufallszahlen zwischen 0 und 1 (exklusiv)
bubble_sort(numbers)
print(numbers)  # sortierte Zufallszahlen
