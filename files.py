# CRUD operations on files

# open file

myFile = open('myfile.txt', 'w')  # w is mode for writing

# get file info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# write to file
myFile.write('this is a test using python')
myFile.write('\nsecond line')
myFile.close()

# append to file
myFile = open('myfile.txt', 'a')  # a is mode for append
myFile.write('\nthis is the third line')
myFile.close()

# read file
print('*******')
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
