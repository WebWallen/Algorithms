#!/usr/bin/python

import sys

def making_change(amount, denominations):
  ways = [0] * (amount + 1)
  ways[0] = 1
  for denomination in denominations:
    for total in range(denomination, amount + 1):
      ways[total] += ways[total - denomination]
  return ways[amount]

print(making_change(30, [1, 5, 10, 25, 50]))
print(making_change(100, [1, 5, 10, 25, 50]))
print(making_change(300, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")