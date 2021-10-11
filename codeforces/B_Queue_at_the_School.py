__author__ = 'Colin Bethea'

def main(t, line):
   while (t > 0):
    t -= 1
    for i in range(len(line)):
       if line[i] != line[i - 1]:
          line[i], line[i - 1] = line[i - 1], line[i]
   return ''.join(line)
 
if __name__ == "__main__":
   [n, t] = list(map(lambda x: int(x), input().split(' ')))
   line = list(input())
   print(main(t, line))
