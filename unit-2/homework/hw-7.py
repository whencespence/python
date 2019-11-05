import random

name = input('Please enter your name (or e to end): ')
messages = ['Good job', 'Have a good day', 'Go to bed']

while name != 'e':
	# randomint accepts two paramaters, lowest and highest, where highest stops at one less than the size of the list
	pos = random.randint(0, len(messages) - 1)
	print(messages[pos])
	name = input('Please enter your name (or e to end): ')