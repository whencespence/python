# Working with *args

# *args works like a list
def add(*args):
	print(len(args))
	total = 0
	# don't use the * inside function - only as params
	for item in args:
		total += item
	return total

# add(1,2)
print(add(1,2,4,5,6,7,8,9,10,11,12,13,14))