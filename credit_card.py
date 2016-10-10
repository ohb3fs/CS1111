# Olivia Bicks ohb3fs

number = input("Type a credit card (just digits): ")
sum_1 = 0
sum_2 = 0
dd_string = ""
if len(number) % 2 == 0:
    for x in range(1, len(number)+1, 2):
        digit = int(number[x])
        sum_1 += digit

    for x in range(0, len(number), 2):
        digit = int(number[x])
        double_digit = str(digit*2).split()
        dd_string += str(double_digit)
    for y in dd_string:
        if '0' <= y <= '9':
            sum_2 += int(y)
    total = sum_1 + sum_2
    if total % 10 == 0:
        print("Yes,", number, "is a valid credit card number")
    else:
        print(number, "is not a valid credit card number")

else:
    for x in range(0, len(number)+1, 2):
        digit = int(number[x])
        sum_1 += digit

    for x in range(1, len(number), 2):
        digit = int(number[x])
        double_digit = str(digit*2).split()
        dd_string += str(double_digit)
    for y in dd_string:
        if '0' <= y <= '9':
            sum_2 += int(y)
    print(sum_1)
    print(sum_2)
    total = sum_1 + sum_2
    if total % 10 == 0:
        print("Yes,", number, "is a valid credit card number")
    else:
        print(number, "is not a valid credit card number")
