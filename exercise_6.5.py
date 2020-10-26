text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
ano_pos = text.find('5', pos)
num = text[pos:ano_pos+1]
print(float(num))