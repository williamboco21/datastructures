# String Concatenation

word = "Hello "
word2 = "World"
new_word = word + word2
print(new_word)
print()

##################################

# Looking Deeper into in
fruit = 'banana'
for letter in fruit:
    print(letter)
print()

##################################

# String Slicing
name = "Kamado Tanjiro"
print(name[0:4])
print(name[7:8])
print(name[7:20])

# If the first or last number is left off
print(name[:2])
print(name[8:])
print(name[:])
print()

###################################

# Using in as a Logical Operator

second_fruit = 'orange'

if 'n' in second_fruit:
    print('Found it!')

if 't' in second_fruit:
    print('Got it!')
else:
    print("t is not in the word.")
print()

###################################

# String comparison

if second_fruit == 'orange':
    print("All right, oranges!")
print()

###################################

# String Library

hello = "Hello Yam"
greet = hello.lower()
print(greet)
print(hello)
print('Hi there!'.lower())
print()

###################################

# Searching in a String

pos = fruit.find('na')
print(pos)
anotha_pos = fruit.find('x')
print(anotha_pos)

###################################

# Making Everything UPPER CASE