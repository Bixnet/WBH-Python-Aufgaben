import random

def fill_entry(self, row, column):
    if row == self.n:
        return True

    if column == self.n - 1:
        next_row, next_col = row + 1, 0
    else:
        next_row, next_col = row, column + 1

    candidates = list(range(1, self.n + 1))
    random.shuffle(candidates)

    for value in candidates:
        if (self.available_in_row(row, value)
                and self.available_in_column(column, value)
                and self.available_in_box(row, column, value)):

            self.field[row][column] = value

            if self.fill_entry(next_row, next_col):
                return True

            self.field[row][column] = 0

    return False