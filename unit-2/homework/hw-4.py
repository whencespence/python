string = 'Python Programming at General Assembly is Awesome!!'
new_string = ''

for character in string:
	if character != ' ' and character != 's' and character != 'm':
		new_string += character
print(new_string)