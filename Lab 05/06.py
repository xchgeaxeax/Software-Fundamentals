def get_sum_even(numbers):
    count = 0
    if numbers == []:
            return count
    else:
        for i in range(len(numbers)):
            try:
                if numbers[i] % 2 == 0:
                    count += numbers[i]
            except TypeError:
                continue
        return count




#my_list = [1, 2, 3.5, 4, -1, 2]
#print(get_sum_even(my_list))
#my_list = [1, 2, 3, 4, "two", 2]
#print(get_sum_even(my_list))
#print(get_sum_even([]))
#print(get_sum_even(['NA']))