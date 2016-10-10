# Olivia Bicks ohb3fs
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def letter_to_index(letter):
    lowercase = letter.lower()
    if lowercase in alphabet:
        index = alphabet.index(lowercase)
        return index
    else:
        return -1


def index_to_letter(index):
    if 0 <= index <= 25:
        letter = alphabet[index]
        return letter
    else:
        return "?"


def vigenere_encrypt(plain_letter, key_letter):
    plain_letter_lower = plain_letter.lower()
    key_letter_lower = key_letter.lower()
    if letter_to_index(plain_letter_lower) == -1:
        return plain_letter
    else:
        converted_to_number = letter_to_index(plain_letter_lower) + letter_to_index(key_letter_lower)
        if converted_to_number >= 26:
            wrapped_around = converted_to_number - 26
            encrypted_letter = alphabet[wrapped_around]
        else:
            encrypted_letter = alphabet[converted_to_number]
        return encrypted_letter


def vigenere_decrypt(cipher_letter, key_letter):
    cipher_letter_lower = cipher_letter.lower()
    key_letter_lower = key_letter.lower()
    encrypted_index = letter_to_index(cipher_letter_lower)
    key_index = letter_to_index(key_letter_lower)
    if encrypted_index != -1 and key_index != -1:
        decrypted_index = encrypted_index - key_index
        if decrypted_index < 0:
            decrypted_letter = index_to_letter(decrypted_index + 26)
            return decrypted_letter
        else:
            decrypted_letter = index_to_letter(decrypted_index)
            return decrypted_letter
    else:
        return cipher_letter


def encrypt(plaintext, key):
    code = ""
    key += key * 1000
    for index, letter in enumerate(plaintext):
        #index = plaintext.index(letter)
        key_letter = key[index]
        encrypted_letter = vigenere_encrypt(letter, key_letter)
        code += encrypted_letter
    return code


def decrypt(ciphertext, key):
    decode = ""
    key += key * 1000
    for index, letter in enumerate(ciphertext):
        key_letter = key[index]
        decrypted_letter = vigenere_decrypt(letter, key_letter)
        decode += decrypted_letter
    return decode


