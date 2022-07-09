# Use words.txt as the file name

fname = input("Enter file name: ")

fh = open(fname)

read_file = fh.read()

read_file = read_file.rstrip()

print(read_file.upper())