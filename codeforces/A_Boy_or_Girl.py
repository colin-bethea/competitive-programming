__author__ = 'Colin Bethea'

def main(name):
   charset = set()
   for char in name:
      charset.add(char) 
   return 'CHAT WITH HER!' if len(charset) % 2 == 0 else 'IGNORE HIM!'
 
if __name__ == "__main__":
   name = input()
   print(main(name))
