# Python has functions for creating, reading, updating, and deleting files.

## Open a file  - 'w' for write mode
f = open('myFile.txt', 'w')

## Get info on file
print("Name: ", f.name)
print("Is Closed: ", f.closed)
print("Mode: ", f.mode)

## Write to file
f.write('My first file in python')
f.write('... second line in my first file')

## Close a file
f.close()
print("Name: ", f.name)
print("Is Closed: ", f.closed)
print("Mode: ", f.mode)

## Append to a file - 'a' for append mode
f = open('myFile.txt', 'a')
f.write('      This is fun!')

## Read from file
f = open('myFile.txt', 'r+')
text = f.read(200)
print(text)