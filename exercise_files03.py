fname = input("Enter a file name: ")
fh = open(fname, 'r')

count = 0
value = 0.0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count = count + 1
        pos = line.find('0')
        end_pos = line.find('\n', pos, -1)
        value = value + float(line[pos:end_pos])

print(f"Average spam confidence: {value / count}")