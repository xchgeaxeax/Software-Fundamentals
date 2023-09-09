def count_multiples():
    integer = int(input("Enter an integer: "))
    filename = input("Enter a filename: ")


    count = 0
    with open(filename, 'r') as file:
        numbers = file.read().split()
        for number in numbers:
            if int(number) % integer == 0:
                count += 1

    if count == 1:
        print("There is 1 multiple of", integer, "in the", "'" + filename + "'", "file.")
    else:
        print("There are", count, "multiples of", integer, "in the", "'" + filename + "'", "file.")

count_multiples()