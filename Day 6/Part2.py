import re

f = open('input.txt')
lines = f.readlines()

answer_group = []
full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    if x == '':
        full_group = []
        for answer in answer_group:
            full_group.append(answer)
            #full_group = full_group + ' ' + answer
        separator =' '
        full_group = separator.join(full_group)
        full_list.append(full_group)
        answer_group = []

    else:
        answer_group.append(x)
    
full_group = []
for answer in answer_group:
    full_group.append(answer)
separator =' '
full_group = separator.join(full_group)
full_list.append(full_group)
answer_group = []

final_pts = 0

for group in full_list:
    group = group.split(' ')
    first_answers = group[0]
    group.pop(0)

    if len(group) != 0:

        common_answers = []
        for question in first_answers:
            common_in_group = []
            for person in group:
                if question in person:
                    common_in_group.append(question)
            if len(common_in_group) == len(group) and len(common_in_group) > 0:
                common_answers.append(common_in_group[0])
            common_in_group = []
        final_pts += len(common_answers)
    
    else:
        final_pts+= len(first_answers)  

print(final_pts)