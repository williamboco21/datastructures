# Opening and reading the text file

file = open('files/data.txt', 'r')
for data in file:
    print(data)
file.close()
print()

###################################

# Counting the number of lines

file = open('files/data.txt', 'r')
count = 0
for line in file:
    count = count + 1
print(f"The number of line/s are: {count}.")
file.close()
print()

###################################

# Reading the Whole File

file = open('files/data.txt')
all = file.read()
print(len(all))
print(all[:20])
file.close()
print()

###################################

# Searching through a file

file = open('files/data.txt')
for data in file:
    if not data.startswith("From:"):
        continue
    print(data.rstrip())
file.close()
print()


###################################

# Skipping with continue

file = open('files/data.txt')
for data in file:
    if not data.startswith("From:"):
        continue
    print(data.rstrip())
file.close()
print()

###################################

# Using in to Select lines

file = open('files/data.txt')
for data in file:
    if not '@gmail.com' in data:
        continue
    print(data.rstrip())
file.close()
