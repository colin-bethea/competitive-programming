__author__ = 'Colin Bethea'

from collections import Counter

def solve(friends):
	solvable = 0
	for consensus in friends:
		if Counter(consensus)['1'] >= 2:
			solvable += 1
	return solvable

if __name__ == "__main__":
	i = 0
	n = int(input())
	friends = list()
	 
	while (i < n):
		friends.append(input())
		i += 1

	print(solve(friends))
