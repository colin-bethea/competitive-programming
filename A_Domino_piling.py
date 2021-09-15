__author__ = 'Colin Bethea'

import math

def main(m, n):
   return math.floor((m * n) / 2)
 
if __name__ == "__main__":
   [m, n] = map(lambda x: int(x), input().split(' '))
   print(main(m, n))