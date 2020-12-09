import re

f = open('input.txt')
lines = f.readlines()

full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    full_list.append(x)


nums_of_valid = 0

for att in full_list:
    att_split = att.split(':')
    target_let = att_split[0].split(' ')[1]
    num1 = int(att_split[0].split(' ')[0].split('-')[0]) - 1
    num2 = int(att_split[0].split(' ')[0].split('-')[1]) - 1
    password = att_split[1]
    password = re.sub(r' ', '', password)

    num_of_targs = 0
    if password[num1] == target_let:
        num_of_targs +=1 

    if password[num2] == target_let:
        num_of_targs +=1 

    if num_of_targs == 1:
        nums_of_valid +=1




print(nums_of_valid)
