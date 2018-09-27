#!/usr/bin/python
from collections import defaultdict

def convert_to_binary(element):
    num = []
    count = 0
    while element > 0:
      bit = element % 2
      if bit == 1:
        count += 1
      num.append(str(element % 2))
      element = int(element / 2)
    num.reverse()
    #return ''.join(num)
    return count


def solution(elements):
  h_elements = defaultdict(lambda: [])  
  for element in elements:
    h_elements[convert_to_binary(element)].append(element)
  ret = []
  for key in sorted(h_elements):
    ret.extend(sorted(h_elements[key]))
  return ret


print solution([5,3,1, 100, 8, 10,20])
