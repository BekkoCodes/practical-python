import csv
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


# returns 44671.15
# cost = portfolio_cost('data/portfolio.csv')

# returns two faulty lines
cost = portfolio_cost('data/missing.csv')
print(f'Total cost: {cost}')
