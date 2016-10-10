# Olivia Bicks ohb3fs

word = input("Please give me a word: ")
number = 0
vowels = "aeiouy"
beginnings = ['ou', 'ei', 'ae', 'eu', 'oi', 'ea', 'oo', "ai", "oa", 'au', 'ay', 'oy', 'aa', 'ao', 'ee',
              'eo', 'ia', 'ie', 'io', 'iu', 'iy', 'oe', 'ua', 'ue', 'ui', 'uo', 'uy', 'ya', 'yo',
              'yi', 'ye', 'yu', 'ey', 'ay']
if word[:2] in beginnings:
    number += 1
if word[:2] in beginnings and word[2] in vowels:
    number += 1
for letter in range(1, len(word)):
    if word[letter] in vowels and word[letter-1] not in vowels:
        number += 1
if word[len(word)-1] == "e":
    number -= 1
if number <= 0:
    number = 1
print("The word", word, "has", number, "syllables.")


