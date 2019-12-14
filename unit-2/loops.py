# name = 'Christina'


# for index in range(0, 10):
# 	print(name);


# print the odd numbers from 1 - 10
# for index in range(0, 10):
# 	if index % 2 == 1:
# 		print(index)


# print the even numbers from 1 - 10
# for index in range(0, 10):
# 	if index % 2 == 0:
# 		print(index)


# print the sum of the even numbers
# total = 0 
# for index in range (1, 11):
# 	if index % 2 == 0:
# 		# total = total + index
# 		total += index
# print(total)


# Loop over your full name and print only vowels
# name = 'Christina Spencer'

# for letter in name:
# 	if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
# 		print(letter)


my_numbers = [3, 5, 17, 11, 21, 53, 10, 27, 45, 80]
smallest = my_numbers[0]

for number in my_numbers:
	if number < smallest:
		smallest = number
print(smallest)