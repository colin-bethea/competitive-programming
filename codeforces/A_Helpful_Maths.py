__author__ = 'Colin Bethea'

def solve(expression):
	arr = []
	for char in expression:
		if (char.isdigit()):
			arr.append(char)
	arr.sort()
	return '+'.join(arr)

if __name__ == "__main__":
	print(solve(input()))