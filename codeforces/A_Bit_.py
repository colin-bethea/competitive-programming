__author__ = 'Colin Bethea'

def main(statements):
  sum = 0
  for statement in statements:
     if '++' in statement:
        sum += 1
     else:
        sum -= 1
  return sum 
   
 
if __name__ == "__main__":
   n = int(input())
   statements = list()
   for i in range(n):
     statements.append(input()) 
   print(main(statements))
