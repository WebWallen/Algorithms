#!/usr/bin/python

import sys

# Rock, paper, scissors = starting array

def rock_paper_scissors(n):
  if n == 0:
    # No moves left to make, so return an empty array
    return [[]] 
  elif n == 1:
    # There's only 1 variation of each move when n = 1
    return [['rock'], ['paper'], ['scissors']] # R P S
  else:
    # Set up an empty array structure then multiply by three (options) to the nth power (permutations)
    all_rps_combos = [[]] * 3 ** n # RR RP RS 
    # Recursive way to calculate every single RPS option for input n
    rps_combos = rock_paper_scissors(n - 1) # RRR RRP RRS / RRRR RRRP RRRS / RRRRR RRRRP RRRRS / RRRRRR RRRRRP RRRRRS
    # Note: we need two counters since we have a placeholder array of current combo and a "final" array for total combos
    j = 0
    # Initialize for loop and set to length of current combos (needs to run through Rock, Paper, and Scissors)
    for i in range(len(rps_combos)):
      all_rps_combos[j] = rps_combos[i] + ['rock']
      # Increment second index after each pass so we can add the permutation for all three variations
      j += 1
      all_rps_combos[j] = rps_combos[i] + ['paper']
      j += 1
      all_rps_combos[j] = rps_combos[i] + ['scissors']
      j += 1
    # Return total
    return all_rps_combos

print(rock_paper_scissors(2))
print(rock_paper_scissors(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')