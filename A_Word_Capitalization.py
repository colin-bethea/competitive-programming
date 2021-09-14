__author__ = 'Colin Bethea'

def solve(word):
	return word[:1].capitalize() + word[1:]

if __name__ == "__main__":
	print(solve(input()))