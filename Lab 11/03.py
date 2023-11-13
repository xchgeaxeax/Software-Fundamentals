# Write a recursive function named get_min_odd(numbers) which takes a list of positive integers as a parameter. This function calculates and returns the smallest odd number in the list. The function should return 9999 if there are no odd numbers in the list.

def get_min_odd(numbers):
    if numbers == []:
        return 9999
    elif numbers[0] % 2 == 1:
        return min(numbers[0], get_min_odd(numbers[1:]))
    else:
        return get_min_odd(numbers[1:])

lst = [6, 4, 5, 9]
print(get_min_odd(lst))
print(get_min_odd([2]))