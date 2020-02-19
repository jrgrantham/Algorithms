#!/usr/bin/python

import argparse

# find max value for selling
# find the smallest values preceeding it for buying

def find_max_profit(prices):
  max_price = max(prices[1:])
  max_price_index = prices.index(max_price)
  min_prince = min(prices[:max_price_index])
  
  return max_price - min_prince

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))