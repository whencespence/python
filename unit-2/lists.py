# cohort_4 = ['Allaina', 'Chizea', 'Clark', 'Daniela', 'Emma', 'Julian', 'Afira', 'Christina', 'Connor', 'Keerthi', 'Kyle', 'Meaghan', 'Sahil', 'Shilaj']

# print(len(cohort_4))
# cohort_4.append('Thing')
# print(type(cohort_4))
# print(cohort_4)
# cohort_4.remove('Julian')
# print(cohort_4)

# # Removes only first occurrence
# cohort_4.remove('Julian')



# values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40, 85.6, 77.1]
# float_values = []
# for value in values:
# 	if type(value) is float:
# 		float_values.append(value)
# print(float_values)



# weights = [[50, 25, 75], [95.7, 38.3, 55.2], [88, 45, 16]]
# averages = []

# for list in weights:
# 	# list_sum variable in outer loop so it captures sum of each/3 loops, not all loops combined
# 	list_sum = 0

# 	for value in list:
# 		list_sum += value
# 	averages.append(list_sum/len(list))

# print(averages)



# for row in range(1, 11):
# 	for col in range(1, row + 1):
# 		# Add end = ' ' in print statement to print * on the same line
# 		print('*', end=' ')
# 	# This print breaks to new line after the loop
# 	print()

# Cleaner version of ^above
# for i in range(11):
# 	print('*' * (i + 1))



# Set all negative readings to 0
# readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

# for i in range(len(readings)):
# 	if readings[i] < 0:
# 		readings[i] = 0
# print(readings)



# Find the index/position of el in the list
el = 25
ages = [15, 17, 27, 35, 12, 25, 55, 40, 31, 30]

for i in range(len(ages)):
	if ages[i] == 24:
		print(i)