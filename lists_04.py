# Best Friends = Strings and Lists because of the split() function

abc = "Surpass Your Limits"
my_list = abc.split()
print(abc)
print(my_list)
print(len(my_list))
print(my_list[0])

# Another exercise using the split() function
phrase = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
for line in phrase:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])