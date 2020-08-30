# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    """Calculates the total market share cost"""
    with open(filename, 'rt') as file:
        next(file)
        total_sum = 0
        for line in file:
            row = line.split(',')
            total_sum += int(row[1]) * float(row[2])
        return total_sum


cost = portfolio_cost('data/portfolio.csv')
print(f'Total cost: {cost}')
