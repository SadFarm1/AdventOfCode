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

full_pass=''
for field in passport:
    full_pass += ' ' + field
full_list.append(full_pass) 

valid_passports = 0
required_fields= ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

i = 0
for passport in full_list:  
    filled_in = 0
    for field in required_fields:
        if field in passport:
            filled_in += 1


            

    valid_data = 0
    if filled_in == 7:            
        height = passport.split('hgt:')
        height = height[1].split(' ')
        height = height[0]
        heightt = height
        

        if 'in' in height:
            height = int(height.replace('in', ''))
            if height >= 59 and height <= 76:
                valid_data += 1
        elif 'cm' in height:
            height = int(height.replace('cm', ''))
            if height >= 150 and height <= 193:
                valid_data += 1
        print('height:', heightt, valid_data)


        birth = passport.split('byr:')
        birth = birth[1].split(' ')
        birth = birth[0]

        if int(birth) >= 1920 and int(birth) <= 2002:
            valid_data += 1

        print('birth' , birth, valid_data)

        issue = passport.split('iyr:')
        issue = issue[1].split(' ')
        issue = int(issue[0])

        if issue >= 2010 and issue <= 2020:
            valid_data += 1

        print('issue' , issue, valid_data)

        exp = passport.split('eyr:')
        exp = exp[1].split(' ')
        exp = int(exp[0])

        if exp >= 2020 and exp <= 2030:
            valid_data +=1

        print('expire' , exp, valid_data)

        hair = passport.split('hcl:')
        hair = hair[1].split(' ')
        hair = hair[0]

        hair_lets = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8' , '9' , '0', '#']

        if hair[0] == '#':
            if len(hair) == 7:
                #print('flag')
                nums = 0
                for let in hair:
                    #print(let)
                    if let in hair_lets:
                        nums +=1

                #print('nums' , nums)
                if nums == 7:
                    valid_data +=1

        print('hair', hair, valid_data)

        eyes_db = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] 

        eyes = passport.split('ecl:')
        eyes = eyes[1].split(' ')
        eyes = eyes[0]

        if eyes in eyes_db:
            valid_data+=1
        
        print('eyes', eyes, valid_data)

        pid = passport.split('pid:')
        pid = pid[1].split(' ')
        pid = pid[0]



        if len(pid) == 9:
            try:
                x = int(pid)
                valid_data+=1
            except:
                pass
        
        print('pid', pid, valid_data)
        print('==================================================')

    if valid_data >= 7:
        valid_passports +=1

        
    if i == -1:

        break

    i +=1




print(valid_passports)
            

        