import csv
import sys


# pcost.py
#
# Exercise 1.32


def portfolio_cost(filename):
    """Calculates the total market share cost"""
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        total_sum = 0
        for row_number, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_sum += nshares * price
            # this catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {row_number}: Bad row: {row}')
        return total_sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
