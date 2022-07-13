fileName = input("Enter file name: ")

fileHandler = open(fileName)

lineCounter = 0

numbers = 0

for line in fileHandler :

    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    position = line.find(":")
    number = line[position + 2 : ]
    floatNumber = float(number)
    numbers = numbers + floatNumber
    lineCounter = lineCounter + 1

print("Average spam confidence: %r" % (numbers / lineCounter))

