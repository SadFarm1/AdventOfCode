import re

f = open('input.txt')
lines = f.readlines()

full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    full_list.append(x * 1000)


x_cord = 0
trees_hit = 0
for line in full_list:
    if line[x_cord] == '#':
        trees_hit += 1
    
    x_cord += 3

print(trees_hit)

