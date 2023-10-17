import random

def bogo_sort(data):
    operations = 0
    is_sorted = False
    operations += 1
    while not is_sorted:
        i = 0
        operations += 1
        while i < len(data) - 1:
            operations += 5
            j = random.randrange(i, len(data))
            data[i], data[j] = data[j], data[i]
            i += 1
        is_sorted = True
        i = 0
        operations += 2
        while i < len(data) - 1:
            is_sorted = is_sorted and not data[i] > data[i + 1]
            i += 1
            operations += 3
    operations += 1
    print(f"Number of operations: {operations}")

random.seed(1)
data = [4, 3, 2, 1]
bogo_sort(data)
print(data)


operations = 0
print()
print()

random.seed(2)
data = [4, 3, 2, 1]
bogo_sort(data)
print(data)
