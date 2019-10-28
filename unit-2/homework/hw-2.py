# Write a program that can calculate the weekly wage of three kinds of employees:
# Full-time workers - who work 40 hours per week and earn $50 per hour
	# For overtime, they are paid $60 per hour
# Part-time workers - who work 20 hours and earn $65 per hour
	# For overtime they are paid $70 per hour
# Contract workers - who earn $120 per hour, but pay 25% tax on their salary
	# Contract workers do not have overtime hours

worker_type = 'part_time'
hours_worked = 50
weekly_wage = 0

# Switch value of weekly_wage, but print once

# If worker is contract
# if worker_type == 'contract':
# 	hours_worked = hours_worked * 120
# 	print("Weekly wage =", hours_worked - (hours_worked * 0.25))

# # If worker is full-time
# elif worker_type == 'full_time':
# 	if hours_worked > 40:
# 		hours_worked = (hours_worked - 40) * 60
# 		print('Weekly wage + overtime =', hours_worked + 2000)
# 	else:
# 		print("Weekly wage =", hours_worked * 50)

# # If worker is part-time
# elif worker_type == 'part_time':
# 	if hours_worked > 20:
# 		hours_worked = (hours_worked - 20) * 70
# 		print('Weekly wage + overtime =', hours_worked + 1300)
# 	else:
# 		print('Weekly wage =', hours_worked * 65)

# print(weekly_wage)