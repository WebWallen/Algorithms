

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n):
  from itertools import permutations
  cheat_array = []
  cheat_array.append(n)
  combinations = list(permutations(range(1, n)))
  for combo in combinations:
    print(combo)
  print(f"Total Permutations: {len(combinations)}")

eating_cookies(3)
eating_cookies(4)
eating_cookies(5)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')