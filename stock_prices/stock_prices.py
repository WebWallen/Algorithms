import argparse

prices = [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]

def find_max_profit(prices):
  # Step 1. Set max profit variable and assign as 0 for now
  max_profit = 0
  # Step 2: Initialize outer loop for purpose of incrementing
  for i in range(len(prices) - 1):
    # Step 3: Initialize inner loop to calculate price difference
    for j in range(i+1, len(prices)): # i+1 because comparing that to j
      # Step 4: Specify i and j symbolize stock price on different days
      today = prices[i]
      tomorrow = prices[j]
      # Step 5: if difference between buy/sell price is greater than current max, update that variable
      if tomorrow - today > max_profit:
        max_profit = tomorrow - today
  return max_profit

print('Max profit: ', find_max_profit(prices))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))