# Olivia Bicks ohb3fs

number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))
number_4 = int(input("Number 4: "))
number_5 = int(input("Number 5: "))

list_1 = [number_1, number_2, number_3, number_4, number_5]
average = sum(list_1) / len(list_1)
range_1 = max(list_1) - min(list_1)

print("You entered:", list_1)
print("The average is:", average)
print("The range is:", range_1)
deleted_item = int(input("Which item do you want to remove? "))

list_1.remove(deleted_item)
average_2 = sum(list_1) / len(list_1)
range_2 = max(list_1) - min(list_1)

print("The new list has the following values:", list_1)
print("The average is:", average_2)
print("The range is:", range_2)


# I learned how to find the maximum, the minimum, and sum using https://docs.python.org/2/library/functions.html



