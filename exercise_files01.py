while True:
    fh = input("Enter the file name: ")

    try:
        file = open(fh, 'r')
        break
    except:
        print("File does not exist.")
        continue

count = 0
for line in file:
    count = count + 1
    print(line.strip())

print(f"\nThere are {count} lines.")
