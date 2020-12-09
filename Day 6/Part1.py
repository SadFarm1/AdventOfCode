import re

f = open('input.txt')
lines = f.readlines()

answer_group = []
full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    if x == '':
        full_group = ''
        for answer in answer_group:
            full_group = full_group + answer
        full_list.append(full_group)
        answer_group = []

    else:
        answer_group.append(x)
    
full_group = ''
for answer in answer_group:
    full_group += answer
full_list.append(full_group)
answer_group = []


final_pts = 0

for group in full_list:
    answered_list = []
    for question in group:
        if question not in answered_list:
            answered_list.append(question)
    final_pts += len(answered_list)


print(final_pts)