__author__ = 'Colin Bethea'

from collections import Counter

def main(games):
   a = Counter(games)['A']
   d = Counter(games)['D']
   if a > d:
      return 'Anton'
   elif a < d:
      return 'Danik'
   else:
      return 'Friendship'
 
if __name__ == "__main__":
   n = int(input())
   games = list(input())
   print(main(games))
