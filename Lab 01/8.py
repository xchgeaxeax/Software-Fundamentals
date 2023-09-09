def print_hollow_square(rows):
    # Print the upper half of the square
    for i in range(rows):
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1 or i == j or i == rows - 1 - j:
                print("*", end="")
            else:
                print(" ", end="")
        print()


num_rows = int(input("Enter number of rows: "))
print_hollow_square(num_rows)