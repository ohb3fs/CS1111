# Olivia Bicks ohb3fs

word = input("Enter a word")
answer = word.upper()
blank_raw = []
for i in range(0, len(word)):
    blank_raw.append('-')
blank = ("[" + ''.join(blank_raw) + "]")
count = 6

while 0 < count <= 6:
    guess_raw = input(blank + " You have " + str(count) + " left, enter a letter: ")
    guess = guess_raw.upper()
    if guess not in answer:
        count -= 1
        print("Incorrect!")
    else:
        total = answer.count(guess)
        for index, letter in enumerate(answer):
            if letter == guess:
                blank_raw[index] = letter
                blank = ("[" + ''.join(blank_raw) + "]")
        if chr(45) not in blank_raw:
            print("You win! The word was", answer)
            break
        else:
            print("Correct!")
else:
    print("You lose! The word was " + answer)


