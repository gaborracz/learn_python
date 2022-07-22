# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file_name = input("Enter a file: ")

file_handler = open(file_name)

counter = dict()

for line in file_handler :

    if not line.startswith('From ') :
        continue
    
    else :
        print(line)
        words = line.split()
        print(words)
        time = words[5]
        print(time)
        time_split = time.split(':')
        print(time_split)
        hour = time_split[0]
        print(time)
        counter[hour] = counter.get(hour, 0) +1

lst = list()

for key, val in counter.items() :
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)

for v,k in lst :
    print(v,k)