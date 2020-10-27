# Many Counters with a Dictionary

# names = dict()
# names['csev'] = 1
# names['cwen'] = 1
# print(names)
# names['cwen'] = names['cwen'] + 1
# print(names)
#

# When We See a New Name
count = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in count:
#         count[name] = 1
#     else:
#         count[name] = count[name] + 1
# print(count)


# The get method for Dictionaries
# if name in count:
#     x = count[name]
# else:
#     x = 0
#
# x = count.get(name, 0)
# print(x)


# Simplified Counting with get()
counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
