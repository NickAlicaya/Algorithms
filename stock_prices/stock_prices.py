#!/usr/bin/python

import argparse
# prices=[800,300,32,500,750,600]
def find_max_profit(prices):
  highest_value=max(prices[1:])
  # print(highest_value)
  tip=prices.index(highest_value)
  # print(tip)
  lowest_range=prices[:tip]
  # print(lowest_range)
  lowest_value=min(lowest_range)
  # print(lowest_value)
  profit=highest_value-lowest_value
  return profit
# print(find_max_profit(prices))
  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  # find highest value in list
  # find the lowest value before or left of list
  # substract lowest value from highest value

