__author__ = 'Colin Bethea'

def main(k, n, w):
   dollars = 0
   for i in range(1, w + 1):
      dollars += k * i
   dollars -= n
   return dollars if dollars > 0 else 0
 
if __name__ == "__main__":
   [k, n, w] = list(map(lambda x: int(x), input().split(' ')))
   print(main(k, n, w))
