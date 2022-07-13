# Dictionaries are memory based key - value stores. It's like a baby database stored i memory.
# Dictionaries are like lists except the use keys instead of numbers to look up values.

purse = dict()

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2

print(purse)

# Counting how often we "see" something:

ccc = dict()

ccc['csev'] = 1
ccc['cwen'] = 1

print(ccc)

ccc['cwen'] = ccc['cwen'] + 1

print(ccc)

# When we see a new name:

counts = dict()

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names :

    if name not in counts :
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

# The get method for dictionaries:

counts_again = dict()

for name in names :
    counts_again[name] = counts_again.get(name, 0) + 1

print(counts_again)

# Dictionaries and files:

count_words = dict()

line = input('Enter a line of text: ') # the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

words = line.split()

print("Words: ", words)
print("Counting ...")

for word in words :
    count_words[word] = count_words.get(word, 0) + 1

print("Counts: ", count_words)

# Using for loops to go through dictionaries:
# Even though dictionaries are not stored in order, 
# we can write a for loop that goes through all the 
# entries in a dictionary - actually it goes through 
# all of the keys in the dictionary and looks up the values.

ddd = { 'chuck' : 1 , 'fred': 42 , 'jan' : 100}

# In a dictionary for loop goes through the keys not the values (like in a list)
for key in ddd :
    print(key, ddd[key])

# Retrieving list of keys and values:

jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}

print(list(jjj))

print(jjj.keys())

print(jjj.values())

# Items will print a tuple:
print(jjj.items())

# Two iteration variabes, this is really awesome:
for key,value in jjj.items() :
    print(key, value)