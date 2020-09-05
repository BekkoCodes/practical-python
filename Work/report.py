# report.py
#
# Exercise 2.5
import csv


def read_portfolio(filename):
    """ computes blablabla of a portfolio file """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

    return portfolio
