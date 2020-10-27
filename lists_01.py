fruit = 'Banana'

try:
    fruit[0] = 'b'
except:
    print("String is immutable. Therefore, it cannot be changed.\n")

print(fruit.lower())





numbers = ['Asta', 'Shinra', 'Midoriya', 2, 4, 12, 63, 21]

for number in numbers:
    if str(number):
        name = number
        print(f"Hello there, {name}!")
    else:
        print(f"Number is {number}.")

print(len(fruit))
print(len(numbers))

friends = ['Mob', 'Tanjiro', 'Todoroki']
for friend in friends:
    print(f"Hello and Welcome, {friend}")

for i in range(len(friends)):
    friend = friends[i]
    print(f"Hello and hi, {friend}.")
