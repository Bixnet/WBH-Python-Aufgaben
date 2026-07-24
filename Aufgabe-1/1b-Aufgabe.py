print("Aufgabe 1b")
'''
Schreiben Sie eine Funktion get words(number), die mithilfe eines Worterbuchs alle be- ¨ kannten Worter, die mit der ¨ ubergebenen Ziffernkombination gebildet werden k ¨ onnen, zur ¨ uckliefert
'''
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

word_list = {"cat", "bat", "act", "dog", "fog", "book"}


def get_combinations(dialed_number):
    if not dialed_number:
        return []
    combination = []

    def backtrack(index, curr_value):
        if index == len(dialed_number):
            combination.append(curr_value)
            return

        digit = dialed_number[index]
        letters = keypad.get(digit, "")

        for i in letters:
            backtrack(index + 1, curr_value + i)

    backtrack(0, "")
    return combination


def get_words(number):
    all_combinations = get_combinations(number)
    found_words = []

    for combo in all_combinations:
        if combo in word_list:
            found_words.append(combo)

    return found_words


value = get_words("228")
print(value)
