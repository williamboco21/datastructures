# Logic statement

count = 0
total = 0

while True:
    inp = input("Enter a number: ")

    if inp.lower() == 'done':
        break

    number = int(inp)
    count = count + 1
    total = total + number

print(f"\nThe average is {total / count}\n")

# Using Lists
my_list = list()

while True:
    inp = input("Enter a number: ")

    if inp.lower() == 'done':
        break

    number = int(inp)
    my_list.append(number)

print(f"\nThe average is {sum(my_list) / len(my_list)}")