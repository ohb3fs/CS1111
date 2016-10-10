# Olivia Bicks ohb3fs

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]
decoded = input("Enter your cipher text: ").lower()
coded = []

for x in decoded:
    if x in alphabet:
        if x == "a":
            new_code = "x"
        elif x == "b":
            new_code = "y"
        elif x == "c":
            new_code == "z"
        else:
            old_code = alphabet.index(x)
            new_code = alphabet[old_code - 3]
    else:
        new_code = x
    coded.append(new_code)
print("The decoded phrase is: ", "".join(coded))


