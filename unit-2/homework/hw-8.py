# Your program should then loop over the list and add the country each destination is located in to the name of the destination, separated by a hyphen

countries = ['Mexico', 'Mexico', 'Jamaica', 'Tahiti', 'USA', 'Thailand', 'Greece', 'Philippines', 'Puerto Rico', 'Jamaica']
destinations = ['Cozumel', 'Cancun', 'Montego Bay', 'Bora Bora', 'Maui', 'Phuket',
'Mykonos', 'Palawan', 'Vieques', 'Negril']

for index in range(len(destinations)):
	destinations[index] += ' - ' + countries[index]
print(destinations)