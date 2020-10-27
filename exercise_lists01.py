fh = open('files/romeo.txt', 'r')
my_list = list()

for line in fh:
    line = line.rstrip().split()
    for i in range(len(line)):
        word = line[i]

        if not word in my_list:
            my_list.append(word)
        else:
            continue

my_list.sort()
print(my_list)
