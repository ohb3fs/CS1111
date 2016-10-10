# Charlotte Searle (css7kv)

temp_celcius = float(input("What is the temperature in Celcius?"))

temp_fahrenheit = temp_celcius * 1.8 + 32

print('It is {temp_fahrenheit} degrees Fahrenheit'.format(temp_fahrenheit = round(temp_fahrenheit, 1)))


try:
    roman = " "
    original_number = int(input("Enter an integer: "))
    number = original_number
    if 1000 <= number < 4000:
        if (number - 1000) > 0:
            number = number - 1000
            roman = roman + "M"
        else:
            roman = "M"
    elif 500 <= number < 1000:
        if (number - 500) > 0:
            number = number - 500
        else: roman = roman + "D"
    elif 100 <= number < 500:
        if (number - 100) > 0:
            number = number - 100
            roman = roman + "C"
        else: roman = roman + "C"
    elif 50 <= number < 100:
        if (number - 50) > 0:
            number = number - 50
            roman = roman + "L"
        else: roman = roman + "L"
    elif 10 <= number < 50:
        if (number - 10) > 0:
            number = number - 10
            roman = roman + "X"
        else: roman = roman + "X"
    elif 5 <= number < 10:
        if (number - 5 ) > 0:
            number = number - 5
            roman = roman + "V"
        else: roman = roman + "V"
    elif 1 <= number < 5:
        if (number - 1) > 0:
            number = number - 1
            roman = roman + "I"
        else: roman = roman + "I"
    print("In Roman Numerals", original_number, "is", roman)
except ValueError:
    print("There was an error with the input score! Enter integers only! ")


if 0 < integer < 10:
        print("In roman numerals", integer, "is", roman_numeral[0])
    elif 10 <= integer < 100:
        print("In roman numerals", integer, "is", roman_numeral[0], roman_numeral[1])
    elif 100 <= integer < 1000:
        print("In roman numerals", integer, "is", roman_numeral[0], roman_numeral[1], roman_numeral[2])
    elif 1000 <= integer < 4000:
        print("In roman numerals", integer, "is", roman_numeral[0], roman_numeral[1], roman_numeral[2], roman_numeral[3])

