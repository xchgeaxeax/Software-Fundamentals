
def no_evens(numbers):
    for x in numbers:
        if x %2 == 0:
            return False
    return True

print(no_evens([2, 2, 3]))