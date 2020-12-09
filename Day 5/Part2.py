import re
import statistics

f = open('input.txt')
lines = f.readlines()

full_list = []
for line in lines:
    x = re.sub(r'\n', '', line)
    full_list.append(x)

seat_ids = []
i = 0
for ticket in full_list:
    ticket_digits = [x for x in ticket]
    row_info = ticket_digits[0:6]
    row_last = ticket_digits[6]
    seat_info = ticket_digits[7:9]
    column_last = ticket_digits[9]
    
    min_row = 0
    max_row = 128

    for info in row_info:
        if info == 'F':
            middleman = max_row - min_row
            middleman = middleman/2

            max_row = max_row - middleman
        elif info == 'B':
            middleman = max_row - min_row
            middleman = middleman/2

            min_row = min_row + middleman

    max_row -= 1

    row = 0
    if row_last == 'F':
        row = int(min_row)
    elif row_last == 'B':
        row = int(max_row)
    



    min_column = 0
    max_column = 8

    for info in seat_info:
        if info == 'L':
            middleman = max_column - min_column
            middleman = middleman/2

            max_column = max_column - middleman
        elif info == 'R':
            middleman = max_column - min_column
            middleman = middleman/2

            min_column = min_column + middleman

    max_column -= 1

    column = 0
    if column_last == 'L':
        column = int(min_column)
    elif column_last == 'R':
        column = int(max_column)
    



    seat_ID = (row * 8) + column

    seat_ids.append(seat_ID)


for x in range(min(seat_ids), max(seat_ids) + 1 ):
    if x not in seat_ids:
        print(x)