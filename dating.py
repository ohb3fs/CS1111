# Olivia Bicks ohb3fs

age = int(input("How old are you? \n"))
if age < 13:
    print("Invalid age")
else:
    minimum_age = int(age / 2 + 7)
    maximum_age = int(age * 2 - 13)
    print("You can date people between", minimum_age, "and", maximum_age, "years old")


