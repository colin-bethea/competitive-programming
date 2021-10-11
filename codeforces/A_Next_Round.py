__author__ = 'Colin Bethea'

def solve(k, scores):
	advanced = 0
	for score in scores:
		if score > 0 and score >= scores[k - 1]:
			advanced += 1
	return advanced

if __name__ == "__main__":
	[n, k] = map(lambda x: int(x), input().split(' '))
	scores = list(map(lambda x: int(x), input().split(' ')))
	print(solve(k, scores))