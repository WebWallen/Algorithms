#!/usr/bin/python

import sys

# Rock, paper, scissors = starting array

def rock_paper_scissors(n):
  from itertools import permutations
  if n == 2:
    two_moves = ['RP', 'RS', 'RR', 'PR', 'PS', 'PP', 'SP', 'SR', 'SS']
    for move in two_moves:
      if move[0] == move[1]:
        print(move)
      else: 
        move = list(permutations(move))
        print(move)

rock_paper_scissors(2)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')