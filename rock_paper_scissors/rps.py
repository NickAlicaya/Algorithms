#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  results_list= []
  options = ['rock', 'paper', 'scissors']

  def recursive_permutations(iterations, result=[]):
    if iterations == 0:
      return results_list.append(result)
    for i in options:
      recursive_permutations(iterations -1, result + [i])
      # print(result)
  recursive_permutations(n)
  # print('xxxxxxxx',results_list)
  return results_list
 


rock_paper_scissors(2)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')