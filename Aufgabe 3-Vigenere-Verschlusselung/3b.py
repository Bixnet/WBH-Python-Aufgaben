class VigenereCipher:
    def __init__(self, alphabet, password):
        self.alphabet = alphabet
        self.password = password

    def __code(self, message, func):
        result = ""
        for i in range(len(message)):
            letter = message[i]
            password_letter = self.password[i % len(self.password)]
            shift = self.alphabet.index(password_letter)

            if letter in self.alphabet:
                position = self.alphabet.index(letter)
                new_position = func(position, shift) % len(self.alphabet)
                result += self.alphabet[new_position]
            else:
                result += letter
        return result

    def encode(self, message):
        return self.__code(message, lambda position, shift: position + shift)

    def decode(self, message):
        return self.__code(message, lambda position, shift: position - shift)


# --- Aufgabe b) ---
cipher = VigenereCipher(
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    password="ace"
)

message = "Dkisg A - Euhkadi yer zetquvpiel By niielt."
print(cipher.decode(message))