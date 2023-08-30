def get_multiples_of_5(numbers):
    multiples_of_5 = []
    if numbers == []:
        return []
    for i in numbers:
        if i % 5 == 0:
            multiples_of_5.append(i)
    return multiples_of_5