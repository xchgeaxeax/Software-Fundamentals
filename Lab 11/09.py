def join_multiply(first_list, second_list, result_list):
    if not first_list:
        return
    join_multiply(first_list[1:], second_list, result_list)
    result_list.insert(-1, list(map(lambda x: first_list[0] * x, second_list)))


list1 = [4, 5]
list2 = [3, 6, 8]
result = []
join_multiply(list1, list2, result)
print(result)
