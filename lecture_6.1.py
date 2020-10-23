# Len Function

fruit = 'banana'
digits = len(fruit)
# print(digits)

# Len Function in a indeterminate loop

# index = 0
# while index < len(fruit):
#     # print(index, fruit[index])
#     index = index + 1

# Len Function in a determinate loop

# for x in fruit:
#     print(x)


#############################################


# Counting the occurrences of letter a
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1

print(f"Total occurrences of a is {count}")


#############################################


# String Slicing
name = 'Monty Python'

# print(name[0:4])
# print(name[6:7])
# print(name[6:20])

##############################################


# Leaving the first and the last number of the slice

print(name[:2])
print(name[8:])
print(name[:])