fhand = open('ex17_sample.txt')

count = 0

for line in fhand:
    count = count + 1

print("Line count: ", count)

fhand = open('ex17_sample.txt')
inp = fhand.read()
print(len(inp))
print(inp[:5])

fhand = open('ex17_sample.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('This') :
        print(line)

fhand = open('ex17_sample.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('This') :
        continue
    print(line)

fhand = open('ex17_sample.txt')
for line in fhand :
    line = line.rstrip()
    if not 'This' in line :
        continue
    print(line)

