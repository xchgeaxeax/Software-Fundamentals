# Write a recursive function, get_max_list(numbers), which takes a list of integers as a parameter. This function returns the largest value in the list. The base case will probably deal with the scenario where the list has just one value. The recursive case will probably call the function recursively using the original list, but with one item removed.
def get_max_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0], get_max_list(numbers[1:]))

print(get_max_list([1, 2, 3, 4, 5]))