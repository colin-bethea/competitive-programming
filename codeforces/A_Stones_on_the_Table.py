__author__ = 'Colin Bethea'

def main(n, stones):
   remove = 0
   for i in range(1, n):
      if (stones[i - 1] == stones[i]):
         remove += 1
   return remove
 
if __name__ == "__main__":
   n = int(input())
   stones = input()
   print(main(n, stones))
