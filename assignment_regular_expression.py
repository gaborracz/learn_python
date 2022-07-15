import re

file_handler = open('regex_sum_1591700.txt')

numbers = list()

for line in file_handler :
    line = line.rstrip()
    number = re.findall('[0-9]+', line)

    if len(number) == 0 :
        continue

    for element in number :
        x = float(element)
        numbers.append(x)

print(int(sum(numbers)))