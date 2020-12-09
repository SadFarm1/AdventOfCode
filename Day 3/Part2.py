import re

f = open('input.txt')
lines = f.readlines()

full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    full_list.append(x * 1000)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_hit = []

for slope in slopes:
    x_dif, y_dif = slope

    trees_slope = 0
    x_cord = 0
    y_cord = 0
    for x in full_list:

        if not y_cord >= len(full_list):
            line = full_list[y_cord]
            if line[x_cord] == '#':
                trees_slope += 1

        x_cord += x_dif
        y_cord += y_dif
    trees_hit.append(trees_slope)


num_mul = 1
for x in trees_hit:
    num_mul = x * num_mul
    





""" 
for line in full_list:
    if line[x_cord] == '#':
        trees_hit += 1

    x_cord += 3 """

print(num_mul)
