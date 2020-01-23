#!/usr/bin/python

import sys

# Rock, paper, scissors = starting array

def rock_paper_scissors(n):
  from itertools import permutations
  two_moves = []
  # three_moves = []
  # four_moves = []
  # five_moves = []
  # six_moves = []
  if n == 2:
    two_moves.append("Rock")
    two_moves.append("Paper")
    combinations = list(permutations(two_moves))
    for combo in combinations:
      print(combo)
    two_moves.remove("Paper")
    two_moves.append("Scissors")
    combinations = list(permutations(two_moves))
    for combo in combinations:
      print(combo)
    two_moves.remove("Rock")
    two_moves.append("Paper")
    combinations = list(permutations(two_moves))
    for combo in combinations:
      print(combo)

rock_paper_scissors(2)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')