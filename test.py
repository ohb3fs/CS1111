def centered_average(list):
    max_num = max(list)
    min_num = min(list)
    list.remove(max_num)
    list.remove(min_num)
    total = 0
    for number in list:
        total += number
    average = total // len(list)
    return average

print(centered_average([1,2,3,4]))

def palindrome(word):
    original = word
    backwards = ""
    for index in range(len(word)-1, -1, -1):
        backwards += word[index]
    if backwards == original:
        return True
    else:
        return False

print(palindrome("hello"))

nice_kids = {}
naughty_kids = {}
presents = {}
santas_list = open("santas_list", "r")
for line in santas_list:
    new_line = line.split(",")
    kid = new_line[0]
    kind = new_line[1]
    present = new_line[2]
    if kind == "nice":
        nice_kids[kid] = present
    else:
        naughty_kids[kid] = present
    if presents in presents:
        presents[present].append(kid)
    else:
        presents[present] = kid




