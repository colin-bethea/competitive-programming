__author__ = 'Colin Bethea'

def main(l, b):
   years = 0
   while b >= l:
      l *= 3
      b *= 2
      years += 1
   return years
 
if __name__ == "__main__":
   [l, b] = list(map(lambda x: int(x), input().split(' ')))
   print(main(l, b))
