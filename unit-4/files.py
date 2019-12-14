# How to read files
my_file = open('lines.txt', 'r') # create the file pointer, where 'r' is the mode
# need path, unless in the current directory

data = my_file.read() # how you access the data

my_file.close() # make sure you open, write/read, then close

print(data)

# Using 'w' (write)
# my_file = open('lines.txt', 'w') # 'w' overwrites everything in the file
# my_file.write('written stuff...')
# my_file.close()

# Using 'a' (append)
my_file = open('lines.txt', 'a') # 'w' overwrites everything in the file
my_file.write('\nwritten stuff appended...') # where '\n' is new line character
my_file.close()


with open('lines.txt', 'r') as my_file: # 'with' excludes need to close file
	data = my_file.read()
print(data)