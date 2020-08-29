# pcost.py
#
# Exercise 1.27

with open('data/portfolio.csv', 'rt') as file:
    next(file)
    total_sum = 0
    for line in file:
        row = line.split(',')
        total_sum += int(row[1]) * float(row[2])
    print(f'Total cost {total_sum}')
