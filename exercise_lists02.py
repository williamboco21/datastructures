fname = input("Enter a file name: ")

if len(fname) < 1:
    fname = "files/data.txt"

fh = open(fname, 'r')
count = 0
for line in fh:
    if not line.startswith("From "):
        continue

    count = count + 1
    line = line.rstrip().split()
    word = line[1]
    print(word)
print(f"There were {count} lines in the file with From as the word")