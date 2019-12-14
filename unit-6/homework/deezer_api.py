import requests
import json


# 1. Make separate API calls to retrieve data for the artists Eminem, Ed Sheeran, and Cardi B
# 2. Write the data for each artist to a separate json file (so you should have
# eminem.json, ed_sheeran.json, cardi_b.json files)
# 3. For each of the artists:
	# a. How many tracks are listed?
	# b. How many albums are listed?
	# c. Count the number of tracks with explicit lyrics
	# d. Which year was the most recent album for each?
# 4. When was the release date for Eminem’s album titled “The Eminem Show”?
# 5. How many tracks are on Ed Sheeran’s album “Shape of You”?
# 6. Which artist(s) collaborated with Cardi B on the track titled “Cardi B”?
# 7. Build a playlist of 10 songs from these 3 artists. Take songs randomly from each artist until you have 10 in total. For each track store the artists name along with the following data: id readable title title_short title_version link duration rank explicit_lyrics explicit_content_lyrics
# 8. Save your playlist to a flie called random_playlist.json


# Get data for artists
# url = 'https://deezerdevs-deezer.p.rapidapi.com/search'
# artists = ['eminem', 'sheeran', 'cardi']
# headers = {
# 		'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
# 		'x-rapidapi-key': "f767ea0455msh91dfc68d815357dp1cf5fajsnfdff6b9baa24"
# 	}
# response = requests.request('GET', url, headers=headers, params=artists[i])
# data = response.json()
# print(response.text)

# Dump Eminem data into file
# with open('eminem_data.json', 'w') as data_file:
# 	data_file.write(json.dumps(data))
# print(json.dumps(data, indent=4))



# Example: https://api.deezer.com/search?q=eminem
# data_list = []
# i = 0
# artists = ['eminem', 'sheeran', 'cardi']

# while i < len(artists):
#     data = requests.get('https://api.deezer.com/search?q=' + artists[i] + ".US?api_token="+ token).json()
#     data_list.append(data)
#     i = i + 1
	

# artists = ['Eminem', 'Sheeran', 'Cardi']
# data = requests.get('https://deezerdevs-deezer.p.rapidapi.com/search' + '?q=' + artists[i] + ".US?api_token="+ token).json()
# data_list.append(data)

# with open('data.json', 'w') as data_file:
# 	data_file.write(json.dumps(data))
# 	json.dump(data_list, data_file)




# USING CLASS
# class ArtistSummary:
# 	def __init__(self, artist, num_songs, num_albums, num_songs_per_album): # Executes when new ArtistSummary is made
# 		self.artist = artist
# 		self.num_songs = num_songs
# 		self.num_albums = num_albums
# 		self.num_songs_per_album = num_songs_per_album
# 		self.songs = []

# Get artist data
def get_artist_data(artist, file_name):
	url = 'https://deezerdevs-deezer.p.rapidapi.com/search/artist'
	querystring = {'q': artist}
	headers = {
		'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com',
		'x-rapidapi-key': 'f767ea0455msh91dfc68d815357dp1cf5fajsnfdff6b9baa24'
	}
	response = requests.request('GET', url, headers=headers, params=querystring)
	data = response.json()
	print(data)

	# Dump artist data into file
	file_name = file_name+'.json'

	with open(file_name, 'w') as file:
		file.write(json.dumps(data, indent=2))

get_artist_data('beyonce', 'beyonce')

	# def add_song(self, title, artist):
	# 	song = {}
	# 	song['title'] = title
	# 	song['artist'] = artist
	# 	self.songs.append(song)

	# def explicit_songs(self, title, artist):