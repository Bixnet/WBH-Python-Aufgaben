import math
import random
import time
from tabulate import tabulate


class Sudoku:
    def __init__(self, n):
        root = math.isqrt(n)
        if root * root != n:
            raise ValueError(f"n={n} ist ungültig: n muss eine Quadratzahl sein (z.B. 4, 9, 16, 25).")

        self.n = n
        self.box_size = root
        self.field = [[0 for _ in range(n)] for _ in range(n)]
        self.fill_entry(0, 0)

    def fill_entry(self, row, column):
        if row == self.n:
            return True

        if column == self.n - 1:
            next_row, next_col = row + 1, 0
        else:
            next_row, next_col = row, column + 1

        candidates = list(range(1, self.n + 1))
        random.shuffle(candidates)  # "Ziehung ohne Zuruecklegen"

        for value in candidates:
            if (self.available_in_row(row, value)
                    and self.available_in_column(column, value)
                    and self.available_in_box(row, column, value)):

                self.field[row][column] = value

                if self.fill_entry(next_row, next_col):
                    return True

                self.field[row][column] = 0  # backtrack

        return False

    def available_in_row(self, row, value):
        return value not in self.field[row]

    def available_in_column(self, column, value):
        for r in range(self.n):
            if self.field[r][column] == value:
                return False
        return True

    def available_in_box(self, row, column, value):
        box_row_start = (row // self.box_size) * self.box_size
        box_col_start = (column // self.box_size) * self.box_size

        for r in range(box_row_start, box_row_start + self.box_size):
            for c in range(box_col_start, box_col_start + self.box_size):
                if self.field[r][c] == value:
                    return False
        return True


# --- Aufgabe e): kann das Programm n=16 bzw. n=25 erzeugen? ---

if __name__ == "__main__":
    for size in [16, 25]:
        start = time.time()
        sudoku = Sudoku(size)
        elapsed = time.time() - start
        print(f"Fertig in {elapsed:.2f} Sekunden.")
        print(tabulate(sudoku.field, tablefmt="double_grid"))
        print()