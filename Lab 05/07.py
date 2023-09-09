def get_valid_input():
    number = -1 #default
    while not 1 <= number <= 10:
        try:
            user_input = input("Enter a number between 1 and 10 inclusive: ")
            number = float(user_input)
        except ValueError:
            continue
    return number

#print("Valid input: {}".format(get_valid_input()))