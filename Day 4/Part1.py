import re

f = open('input.txt')
lines = f.readlines()

full_list = []
passport = []
for line in lines:
    x = re.sub(r'\n', '', line)
    if x == '':
        full_pass = ''
        for field in passport:
            full_pass += ' ' + field
        full_list.append(full_pass) 
        passport = []
    else:

        passport.append(x)

full_pass = ''
for field in passport:
    full_pass += full_pass + ' ' + field
full_list.append(full_pass) 


valid_passports = 0
required_fields= ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

i = 0
for passport in full_list:  
    filled_in = 0
    for field in required_fields:
        if field in passport:
            filled_in += 1

    print(filled_in)
    if filled_in == 7:
        valid_passports += 1



    i +=1



print(valid_passports)
            

        