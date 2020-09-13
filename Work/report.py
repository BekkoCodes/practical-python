# report.py
#
# Exercise 2.7
import csv


def read_portfolio(filename):
    """ generates a list of dictionaries based on portfolio data """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

    return portfolio


def read_prices(filename):
    """ generates a dictionary based on price data """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) < 2:
                continue
            prices[row[0]] = float(row[1])

    return prices


def compute_gain_loss():
    portfolio = read_portfolio('data/portfolio.csv')
    prices = read_prices('data/prices.csv')
    portfolio_value = 0.0
    current_value = 0.0

    for stock in portfolio:
        name = stock['name']
        portfolio_value += float(stock['price']) * int(stock['shares'])
        if name not in prices:
            print(f'no price for {name} found')
            continue
        current_value += prices[stock['name']] * int(stock['shares'])

    print(f'total cost = {portfolio_value}\ngain = {portfolio_value - current_value}')


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = int(stock['shares'])
        price = float(prices[name])
        change = price - float(stock['price'])
        report.append((name, shares, price, change))
    return report
