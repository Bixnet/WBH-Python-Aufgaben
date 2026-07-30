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
        return value not in self.field[row]

    def available_in_column(self, column, value):
        for row in range(self.n):
            if self.field[row][column] == value:
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


if __name__ == "__main__":
    sudoku = Sudoku(9)
    print(tabulate(sudoku.field, tablefmt="double_grid"))