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
# Time Complexity: O(N^2)
print('Max profit: ', find_max_profit(prices))

# Another take on the same algorithm that aims to reduce time complexity

def faster_max_profit(prices):
  # Step 1: initialize variables needed to perform comparisons (set max to 0)
  max_profit = 0
  # Step 2: set lowest price to first array index because it is automatically current lowest
  lowest_price = prices[0]
  # Step 3: begin for loop of prices array (no weird math as there are no sub-loops)
  for price in prices:
    # Step 4: compare lowest price with current price to determine which is smaller (hint: min makes this easy)
    lowest_price = min(lowest_price, price)
    # Step 5: subtract lowest price from current price to calculate loss/gain and set to variable (price difference)
    price_difference = price - lowest_price
    # Step 6: determine max profit by comparing current max to price differences stored in memory (hint: max makes this easy)
    max_profit = max(max_profit, price_difference)
  return max_profit
# Time Complexity: O(N)
print('Faster max profit: ', faster_max_profit(prices))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))