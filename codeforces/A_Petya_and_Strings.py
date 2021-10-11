__author__ = 'Colin Bethea'

def solve(str1, str2):
	str1, str2 = str1.lower(), str2.lower()
	if str1 == str2:
		return 0
	ptr = 0
	while ptr < len(str1):
		if str1[ptr] == str2[ptr]:
			ptr += 1
		elif str1[ptr] > str2[ptr]:
			return 1
		else:
			return -1

if __name__ == "__main__":
	for i in range(1):
		print(solve(input(), input()))