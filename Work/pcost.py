import csv
import sys


# pcost.py
#
# Exercise 1.32


def portfolio_cost(filename):
    """Calculates the total market share cost"""
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)
        total_sum = 0
        for line in rows:
            try:
                total_sum += int(line[1]) * float(line[2])
            except ValueError:
                print('wrong data format in line\n', line)
        return total_sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
