# my_number = 5
# def high_low(num):
# 	# print "high!" if variable is greater than 10
# 	if num > 10:
# 		print("high!")
# 	else:
# 		print("low!")
# high_low(5)


# Write a program to calculate the sum of all the even numbers between 1000 and 10,000
even_numbers = 0

for index in range (1000, 10000):
	if index % 2 == 0:
		even_numbers += index
print("The sum of even numbers between 1000 and 10,000 is:", even_numbers)