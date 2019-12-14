# Find shortest word in string
def find_short(s):
	return min(len(x) for x in s.split())