import math
from tabulate import tabulate


class Sudoku:
    def __init__(self, n):
        root = math.isqrt(n)
        if root * root != n:
            raise ValueError(f"n={n} ist ungültig: n muss eine Quadratzahl sein (z.B. 4, 9, 16).")

        self.n = n
        self.box_size = root

        self.field = [[0 for _ in range(n)] for _ in range(n)]

        self.fill_entry(0, 0)

    def fill_entry(self, row, column):
        return False

    def available_in_row(self, row, value):
        return False

    def available_in_column(self, column, value):
        return False

    def available_in_box(self, row, column, value):
        return False


if __name__ == "__main__":
    sudoku = Sudoku(9)
    print(tabulate(sudoku.field, tablefmt="double_grid"))
