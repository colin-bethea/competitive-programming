__author__ = 'Colin Bethea'

def main(m):
   x, y = None, None
   for row in range(len(m)):
    for col in range(len(m[row])):
       if m[row][col] == 1:
          x, y = (row + 1, col + 1)
   ans = abs(x - 3) + abs(y - 3)
   return ans 
 
if __name__ == "__main__":
   m = list()
   for i in range(5):
      m.append(list(map(lambda x: int(x), input().split(' ')))) 
   print(main(m))
