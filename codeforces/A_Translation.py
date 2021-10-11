__author__ = 'Colin Bethea'

def main(original, new):
   return 'YES' if original[::-1] == new else 'NO'
 
if __name__ == "__main__":
   original = input()
   new = input()
   print(main(original, new))