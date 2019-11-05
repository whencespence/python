marvel_movies = ['Iron Man','Iron Man 2', 'Captain America', 'The Incredible Hulk', 'The Worst', 'Guardians of the Galaxy']
special_marvel_movies = []

for movie in marvel_movies:
	if 'the ' in movie.lower() or ' the ' in movie.lower():
		special_marvel_movies.append(movie)
print(special_marvel_movies)