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
  elif n == 3:
    three_moves = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS', 
    'PPP', 'PPR', 'PPS', 'PRR', 'PRS', 'PRP', 'PSS', 'PSR', 'PSP', 
    'SSS', 'SSR', 'SSP', 'SRR', 'SRS', 'SRP', 'SPS', 'SPP', 'SPR']
    for move in three_moves:
      if move[0] == move[1] and move[0] == move[2] and move[2] == move[1]:
        print(move)
      elif move[0] == move[2]:
        print(move)
      else:
        move = list(permutations(move))
        print(move)
rock_paper_scissors(2)
rock_paper_scissors(3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')