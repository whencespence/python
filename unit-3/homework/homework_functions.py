# PROBLEM 1
# Write a function called reverse_list that accepts a list, and returns a copy of the list with the items in reverse order
classmates = ['first', 'second', 'third']

def reverse_list(list):
	new_list = list.reverse()
	return new_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(classmates))



# PROBLEM 2
# Write a function called encode_string that accepts a string of letters,
# and returns a new string with the letters replaced with their corresponding
# number position in the alphabet

# def encode_string(string):
# 	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	# for character in string:
	# 	if character in string 



# PROBLEM 3
# Write a function called pivot_split that accepts two arguments: a list of integers and an integer, called pivot
def pivot_split(my_list, my_num):
	left = []
	right = []
	for num in my_list:
		if num < my_num:
			left.append(num)
		else:
			right.append(num)
	# returns two lists / builds lists on this line
	return [left, right]

print(pivot_split([12, 7, 8, 15,3, 9, 11, -7], 8))



# PROBLEM 4
# Write a function called is_isogram that returns true if all the letters in a string are unique (no reapeated characters), or returns false otherwise
def is_isogram(string):
	already_seen = []
	for character in string:
		if character is already_seen:
			return False
		else:
			already_seen.append(character)
	return True

print(is_isogram('hello'))