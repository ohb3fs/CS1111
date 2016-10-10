# Olivia Bicks ohb3fs


original_integer = int(input("Enter an integer: "))
integer = original_integer
roman_numeral = []
if 0 < integer < 4000:

    conversion = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40],
                  ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]

    for letter, value in conversion:
        while (integer - value) >= 0:
            roman_numeral.append(letter)
            integer -= value
    if len(roman_numeral)==1:
        print("In roman numerals", original_integer, 'is', roman_numeral[0])
    elif len(roman_numeral) ==2:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1])
    elif len(roman_numeral) == 3:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2])
    elif len(roman_numeral) == 4:
        print ("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3])
    elif len(roman_numeral) == 5:
        print ("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4])
    elif len(roman_numeral) == 6:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5])
    elif len(roman_numeral) == 7:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6])
    elif len(roman_numeral) == 8:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6] + roman_numeral[7])
    elif len(roman_numeral) == 9:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6] + roman_numeral[7] +
              roman_numeral [8])
    elif len(roman_numeral) == 10:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6] + roman_numeral[7] +
              roman_numeral[8] + roman_numeral[9])
    elif len(roman_numeral) == 11:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6] + roman_numeral[7] +
              roman_numeral[8] + roman_numeral[9] + roman_numeral[10])
    elif len(roman_numeral) == 12:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6] + roman_numeral[7] +
              roman_numeral[8] + roman_numeral[9] + roman_numeral[10] + roman_numeral[11])
    elif len(roman_numeral) == 13:
        print("In roman numerals", original_integer, 'is', roman_numeral[0] + roman_numeral[1] + roman_numeral[2]
               + roman_numeral[3] + roman_numeral[4] + roman_numeral[5] + roman_numeral[6] + roman_numeral[7] +
              roman_numeral[8] + roman_numeral[9] + roman_numeral[10] + roman_numeral[11] + roman_numeral[12])
else:
    print("Input must be between 1 and 3999")


