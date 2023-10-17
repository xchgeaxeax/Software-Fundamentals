def get_min_abs_distance(a_list):
    # min_distance = 0
    distence = []
    for i in range(len(a_list) - 1):
        current_distance = abs(a_list[i] - a_list[i + 1])
        distence.append(current_distance)
        # print(current_distance)
    min_distance = min(distence)
    return min_distance

print(get_min_abs_distance([20, 4, 6, 19, 6, 5]))