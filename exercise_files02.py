fname = input("Enter the filename: ")

fh = open(fname, 'r')

for line in fh:
    print(line.upper().strip())