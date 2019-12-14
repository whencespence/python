### Sets
colours = {'red', 'orange', 'green', 'blue', 'yellow', 'indigo', 'purple'} # <class 'set'>
print(type(colours))

values = [1, 2, 3, 4, 5, 2, 5, 2]
unique_values = set(values)
print(unique_values)



# Create single line function is_isogram
def is_isogram(string):
	# unique = set(string)
	# if len(unique) == len(string):
	# 	return True
	# else:
	# 	return False
	return len(set(string)) == len(string) # will return if true
	
is_isogram("happy")

### Tuples
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')