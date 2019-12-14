# Dictionary and key/value pairs
student = {'name': 'Christina', 'age': '10', 'city': 'Toronto'}

# Access elements in dictionary using dictionary name followed by key
print(student['name'], student['age'], student['city'])

# Dictionary cannot have duplicate keys

car = {} # creates empty dictionary
car['make'] = 'Toyota' # adding items to dictionary...
car['model'] = 'Prius'
car['year'] = 2019
car['color'] = 'silver'

for item in car:
	print(item) # prints keys
	print(car[item]) # prints values


# List of dictionaries
cars = [
	{'year': '2000', 'make': 'Toyota', 'colour': 'black'},
	{'year': '2001', 'make': 'Ford', 'colour': 'white'},
	{'year': '2002', 'make': 'Acura', 'colour': 'red'},
	{'year': '2003', 'make': 'Toyota', 'colour': 'red'}
]

# print(cars[0]) # print by index
total = 0
for car in cars:
	if car['make'] == 'Toyota':
		total += 1
print(total)

print(student.keys())
print(student.values())
print(student.items())


for key, value in student.items(): # returns/iterates over compound values
	print(key, value)