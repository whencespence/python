# PROBLEM 1
# Write a function called frequency_counter that accepts a string, and returns a dictionary with the number of times each character occurs in the string
def frequency_counter(str):
	dict = {}
	for char in str:
		keys = dict.keys()
		if char in keys:
			dict[char] += 1
		else:
			dict[char] = 1
	return dict
print(frequency_counter('christina'))



# PROBLEM 2
# Function accepts a person list (which is a list of lists), and returns a dictionary. Each list in the person list has only two items. The keys of your result dictionary should be the first item in each list, and the value should be the second item
# def list_to_dict(person_list):