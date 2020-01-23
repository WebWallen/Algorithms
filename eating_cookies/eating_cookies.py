import sys

# Eating cookies take two (think I thought this through with equations used during lecture on my mind)

def eating_cookies(n, cache):
  # There is only one way to eat zero cookies.
  if n == 0:
    return 1
  # If n = 1 (1 way to eat). If n = 2 (2 ways to eat)
  elif n <= 2:
    return n
  # Store data in cache for ALL variations of n to save and prevent needless repetition/time complexity
  elif cache[n] > 0:
    return cache[n]
  # Use cache with recursive calls for the same reason. Saves each result to the cache for ease of operations
  cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
  # N = 20. 19, 18, 17. 18, 17, 16. 17, 16, 15... (three callbacks for each num to match the three returns above?)
  return cache[n]

# I can't explain exactly why this works but it does. Same formula we used for Fibonacci with one extra equation.
n = 500
cache = {i: 0 for i in range (n + 1)}

print(eating_cookies(n, cache))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')

# This is wrong but I'm keeping it just in case it's helpful later
def permutation_practice(n):
  from itertools import permutations
  convert_num_to_array = []
  convert_num_to_array.append(n)
  combinations = list(permutations(range(1, n)))
  # for combo in combinations:
    # print(combo)
  print(f"Total Permutations: {len(combinations)}")

permutation_practice(3)
permutation_practice(4)
permutation_practice(5)