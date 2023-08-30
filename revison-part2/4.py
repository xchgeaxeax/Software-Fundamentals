def get_sum_positive_even(numbers):
    if numbers == []:
        return 0
    sum = 0
    for i in numbers:
        if i > 0 and i % 2 == 0:
            sum += i
    return sum

#get_sum_positive_even([1,2,3,4,5,-1,-9])