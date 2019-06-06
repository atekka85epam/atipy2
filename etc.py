#!/usr/bin/env python2
### Original Repo http://hacked2bits.com/software/python-challenge/

file_name = "test.txt"
with open(file_name, 'r') as f:
    file_data = f.read()

characters = []
data = list(file_data)

for i in range(len(data)):
    if (65 <= ord(data[i]) <= 90) or (97 <= ord(data[i]) <= 122):
        characters.append(data[i])

text = "".join(characters)
print (text)