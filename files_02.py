# Prompt for File Name

# filename = input("Enter the file name: ")
# file = open(filename, 'r')
# for data in file:
#     print(data)
# file.close()


##################################

# Try / Except for Bad file names

filename = input("Enter the file name: ")

try:
    file = open(filename, 'r')
except:
    print("The filename does not exist.")
    quit()

count = 0
for data in file:
    print(data.rstrip())