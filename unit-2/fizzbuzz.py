'''
for all numbers from 1 - 50
if it's a multiple of 3, print 'fizz'
if it's a multiple of 5, print 'buzz'

if it's a multiple of 15, print 'fizzbuzz'
otherwise print the number
'''

for num in range(1, 51):
	if num % 15 == 0:
		print('fizzbuzz')
	elif num % 3 == 0:
		print('fizz')
	elif num % 5 == 0:
		print('buzz')
	else:
		print(num)