rows = int(input('Enter number of rows: '))
for i in range(2,rows + 2):
    for j in range(1, i):
        print(j, end=' ')
    print()