import string

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



alphabet = "abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = "TEuOu QWQQvCqyu yOI uPLxH HzxSyAGEwAG, KtAG tKsD JyzxP?"


possible_passwords = [a + b for a in string.ascii_lowercase for b in string.ascii_lowercase]
print(f"Total passwords to try: {len(possible_passwords)}")   # 676


ciphers = [VigenereCipher(alphabet=alphabet, password=pw) for pw in possible_passwords]


results = {pw: c.decode(ciphertext) for pw, c in zip(possible_passwords, ciphers)}


common_words = [" und ", " der ", " die ", " das ", " ist ", " nicht ", " ein ", " du ", " ich ", " wir ", " wie "]
for pw, text in results.items():
    lowered = " " + text.lower() + " "
    if any(w in lowered for w in common_words):
        print(pw, "->", text)