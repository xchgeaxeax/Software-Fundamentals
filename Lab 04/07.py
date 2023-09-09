def get_index_of_largest(numbers):
    if len(numbers) == 0:
        return -1
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return numbers.index(max_value)

#print(get_index_of_largest([51, 65, 66, 80, -10, 55]))