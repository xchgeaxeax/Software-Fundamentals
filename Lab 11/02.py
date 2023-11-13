def get_sum_digits(number):
    if number // 10 == 0:
        return number
    else:
        return get_sum_digits(number // 10) + number % 10


print(234, ":", get_sum_digits(234))
print(106, ":", get_sum_digits(106))
