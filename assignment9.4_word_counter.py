# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.

fileName = input("Enter a file: ")

fileHandler = open(fileName)

count_senders = dict()

top_sender = None

top_count = None

for line in fileHandler :

    if not line.startswith('From ') :
        continue

    else :
        words = line.split()
        sender = words[1]
        count_senders[sender] = count_senders.get(sender, 0) + 1

for k, v in count_senders.items() :

    if top_count is None or v > top_count :
        top_count = v
        top_sender = k

print(top_sender, top_count)