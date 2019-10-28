# Write a program that will calculate the number of spaces in the following string: 'Python Programming at General Assembly is Awesome!!'

string = 'Python Programming at General Assembly is Awesome!!'
spaces = 0

for letter in string:
	if letter == ' ':
		spaces += 1
print(spaces)