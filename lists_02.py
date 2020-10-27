# Concatenating Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)
print(b)
print((c))
print()

# List Slicing

my_list = [24, 8, 81, 21, 60, 26]
print(my_list[1:3])
print(my_list[:4])
print(my_list[3:])
print(my_list[:])
print()

# Is Something in a List?
if 24 in my_list:
    print("Yehey")

if 15 in my_list:
    print("Ohh no this will not print")

if not 20 in my_list:
    print("This will print yehey!")

print()


# Sorting the List
my_list.sort()
print(my_list)