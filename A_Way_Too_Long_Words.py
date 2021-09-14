__author__ = 'Colin Bethea'

def solve(n, word):
	# Handle (<= n) case
	if len(word) <= 10:
		return word
	# Handle standard case
	start, end = word[0:1], word[-1:]
	sliced = len(word[1:-1])
	# Return spliced string
	return start + str(sliced) + end


if __name__ == "__main__":
    i = 0
    words = list()
    n = int(input())

    while (i < n):
        words.append(input())
        i += 1

    for idx in range(n):
        print(solve(n, words[idx]))
