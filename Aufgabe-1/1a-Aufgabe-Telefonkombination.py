'''a) Schreiben Sie eine Funktion get combinations(number), die fur eine gegebene Ziffern- ¨
kombinationen eine Liste aller moglichen Buchstabenkombinationen zur ¨ uckliefert. ¨
Beispielaufrufe:'''

keypad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


# enter a number
def get_combinations(dialed_number):
    if not dialed_number:
        return []
    combination = []

    def backtrack(index, curr_value):
        # when the index reaches the end, stop
        if index == len(dialed_number):
            combination.append(curr_value)
            return

        # Indexing: count,retrieve the dialed number
        digit = dialed_number[index]
        # print(digit)

        # retrieve the letter in the dialed number
        letters = keypad.get(digit, "")
        # print(letters)

        # loop through the letter
        for i in letters:
            # move to the next digit
            backtrack(index + 1, curr_value + i)

    # First call-starts the process-start from 0
    backtrack(0, "")
    return combination


value = get_combinations("23")
print(value)
