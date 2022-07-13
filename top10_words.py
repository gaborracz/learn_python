file_name = input("Enter a file name: ")

file_handler = open(file_name)

counts = dict()

for line in file_handler :
    words = line.split()

    for word in words :
        counts[word] = counts.get(word, 0) + 1

lst = list()

for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val, key in lst[:10] :
    print(key, val)