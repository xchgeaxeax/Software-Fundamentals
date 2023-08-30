str1 = ''
for i in range(200,300):
    if i % 5 == 0 and i % 3 != 0:
        str1 += str(i) +','

print(str1[0:len(str1) - 1])


