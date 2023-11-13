odd_list = []
def get_odds_list(numbers):
    global odd_list
    # if 'result' not in dir():
    #     result = []
    if numbers:
        if numbers[0] % 2 != 0:
            odd_list.append(numbers[0])
        return get_odds_list(numbers[1:])
    else:
        result = odd_list
        odd_list = []
        return result


print(get_odds_list([2, 3, 5, 6]))
print(get_odds_list([2, 4, 6, 8]))
