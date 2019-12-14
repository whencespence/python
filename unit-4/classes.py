from random import shuffle
import json



# class Person:
# 	# every class must have init method - function defined inside the class
# 	# dunder method - 'double underscore' method
# 	# When you create objects you initialize functions within
# 	# 'self' keeps track of its own data ---> 'self' = 'this' in JS
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def say_hello(self):
# 		print(f'Say hello {self.name}')

# # How to instantiate a class...
# p = Person('Apollo', 64)
# print(type(p)) # Prints the module that holds the class ---> <class '__main__.Person'>
# p.say_hello()



# Create rectangle class, with a length and width, and two methods, perimeter and area
# class Rectangle:
# 	def __init__(self, length, width):
# 		self.length = length
# 		self.width = width

# 	def perimeter(self): # have to pass 'self'
# 		return (self.length + self.width) * 2

# 	def area(self):
# 		return self.length * self.width

# r = Rectangle(2, 4) # Creates a rectangle instance/object of the class with values, now accessible to use class methods 'perimeter' and 'area'
# print(r.perimeter())
# print(r.area())



# Create a playlist class that has a name and list of tracks
# Each list of tracks is a dictionary, with title, artist, length of track
# Write methods to add a track, remove a track, and shuffle the playlist
track_file_name = 'tracks.txt'

class Playlist:
	def __init__(self, name): # Executes when a new playlist is created
		self.name = name
		self.tracks = []

	def add_track(self, title, artist, length):
		track = {}
		track['title'] = title
		track['artist'] = artist
		track['length'] = length
		self.tracks.append(track)
		
	def remove_track(self, title):
		for index in range(len(self.tracks)):
			if title == self.tracks[index]['title']: # self.tracks is name of list, where each item is represented as 'index', looking at the key 'title'
				break
		self.tracks.pop(index)
	
	def save_tracks(self):
		# open file for writing
		with open(track_file_name, 'w') as track_file:
			for track in self.tracks:
				track_file.write(json.dumps(track, indent=2)) # converts dictionary into a string

			# track_file.write(json.dumps(self.tracks, indent=2)) # Or, remove for loop to dump entire list

	def load_tracks(self):
		# load data from tracks.txt file
		with open('tracks.txt', 'r') as my_file: # 'with' excludes need to close file
			data = my_file.load()
		# set the tracks variable to the data
		print(data)

	# def __repr__(self): # representation / can return only a string
	# 	return f'name: {self.name}, tracks: {self.tracks}'

	# def shuffle_playlist(self):
	# 	self.tracks.random.shuffle(self.tracks)

p1 = Playlist('tunes')
p1.add_track('Song', 'Beatles', 2.00)
p1.add_track('Another Song', 'Band', 3.50)
p1.add_track('Best Song', 'The Band', 2.50)
p1.add_track('Better Song', 'Beatles', 2.80)
p1.save_tracks()

new_playlist = Playlist('new_tunes')
new_playlist.load_tracks()

# print(p1)
# p.remove_track()
# p.shufflePlaylist()