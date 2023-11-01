def no_evens(numbers):
    if len(numbers) == 1:
        return numbers[0] % 2 != 0
    else:
        if numbers[0] % 2 == 0:
            return False
        else:
            return no_evens(numbers[1:])


print(no_evens([2, 3, 5, 6]))
print(no_evens([2]))
print(no_evens([1, 3, 5, 7]))
