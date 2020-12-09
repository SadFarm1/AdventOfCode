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
    min_num = int(att_split[0].split(' ')[0].split('-')[0])
    max_num = int(att_split[0].split(' ')[0].split('-')[1])
    password = att_split[1]
    password = re.sub(r' ', '', password)

    num_of_targs = 0
    for letter in password:
        if letter == target_let:
            num_of_targs += 1

    
    if num_of_targs >= min_num and max_num >= num_of_targs:
        nums_of_valid += 1



print(nums_of_valid)
