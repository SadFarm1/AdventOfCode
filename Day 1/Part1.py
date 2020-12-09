import requests
import json
import re

f = open('input.txt')
lines = f.readlines()

full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    full_list.append(x)

final_num = 0

full_list_sec = []
for x in full_list:
    full_list_sec.append(int(x))

i = 0
for x in full_list_sec:
    num1 = full_list_sec[i]

    for y in full_list_sec:
        if num1 + y == 2020:
            final_num = num1 * y



    i+= 1


print(final_num)