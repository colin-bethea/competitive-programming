__author__ = 'Colin Bethea'

from collections import Counter

def main(year):
   ans = None
   while not ans:
      if (len(Counter(str(year))) == str(year)):
         ans = year
         break 
      year += 1
   return ans
 
if __name__ == "__main__":
   print(main(int(input())))
