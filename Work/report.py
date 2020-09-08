# report.py
#
# Exercise 2.6
import csv


def read_portfolio(filename):
    """ generates a list of dictionaries based on portfolio data """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

    return portfolio


def read_prices(filename):
    """ generates a dictionary based on price data """
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if len(row) < 2:
                continue
            prices[row[0]] = float(row[1])

    return prices
