# Olivia Bicks ohb3fs

import random


number = int(input("What should the answer be? \n"))
if number == -1:
    answer = random.randint(0, 100)
else:
    answer = number

count = 0
while count < 5:
    guess = int(input("Guess a number: "))
    if guess == answer:
        print("You win! ")
        count = 5
        exit()
    elif guess < answer:
        print("The number is higher than that")
        count = count + 1
    elif guess > answer:
        print("The number is lower than that")
        count = count + 1
print("You lose; the number was", answer)


# I used this website for while loops http://www.tutorialspoint.com/python/python_while_loop.htm





