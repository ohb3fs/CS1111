# Olivia Bicks ohb3fs


entry_1 = input("Add an entry to the phone book ")
entry_2 = input("Add an entry to the phone book ")
entry_3 = input("Add an entry to the phone book ")
entry_4 = input("Add an entry to the phone book ")
entry_5 = input("Add an entry to the phone book ")
contacts = [entry_1.split(' '), entry_2.split(' '), entry_3.split(' '), entry_4.split(' '), entry_5.split(' ')]


name_1 = contacts[0][0]
number_1 = contacts[0][1]
name_2 = contacts[1][0]
number_2 = contacts[1][1]
name_3 = contacts[2][0]
number_3 = contacts[2][1]
name_4 = contacts[3][0]
number_4 = contacts[3][1]
name_5 = contacts[4][0]
number_5 = contacts[4][1]

phone_book_name = {name_1: number_1, name_2: number_2, name_3: number_3, name_4: number_4, name_5: number_5}
phone_book_number = {number_1: name_1, number_2: name_2, number_3: name_3, number_4: name_4, number_5: name_5}

contact_name = input("Who do you want to call? ")
if contact_name in phone_book_name:
    print(contact_name, "'s number is", phone_book_name.get(contact_name))
else:
    print("That name is not in the phone book.")

contact_number = input("Which number do you want to lookup? ")
if contact_number in phone_book_number:
    print("That number belongs to", phone_book_number.get(contact_number))
else:
    print("That number is not in the phone book.")



