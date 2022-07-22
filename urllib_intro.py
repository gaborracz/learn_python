"""
    Since HTTP is so common, we have a library that does
    all the socket work for us and makes web pages look like 
    a files.
"""

import urllib.request, urllib.parse, urllib.error

file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


for line in file_handler :
    print(line.decode().rstrip())


"""
    It works like a file:
"""

file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

loop = 0

for line in file_handler :
    words = line.decode().split()

    for word in words :
        counts[word] = counts.get(word, 0) + 1

print(counts)