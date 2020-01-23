import sys

# Eating cookies take two (think I thought this through with equations used during lecture on my mind)

def eating_cookies(n):
  # There is only one way to eat zero cookies.
  if n == 0:
    return 1
  # If n = 1 (1 way to eat). If n = 2 (2 ways to eat)
  if n <= 2:
    return n
  # N = 20. 19, 18, 17. 18, 17, 16. 17, 16, 15... (three callbacks for each num to match the 3 above?)
  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# I can't explain exactly why this works but it does. Same formula we used for Fibonacci with one extra equation.

print(eating_cookies(3))
print(eating_cookies(5))
print(eating_cookies(10))
print(eating_cookies(100))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# This is wrong but I'm keeping it just in case it's helpful later
def permutation_practice(n):
  from itertools import permutations
  cheat_array = []
  cheat_array.append(n)
  combinations = list(permutations(range(1, n)))
  # for combo in combinations:
    # print(combo)
  print(f"Total Permutations: {len(combinations)}")

permutation_practice(3)
permutation_practice(4)
permutation_practice(5)