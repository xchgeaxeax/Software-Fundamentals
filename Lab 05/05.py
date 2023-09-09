def get_max(numbers):
    try:
        max_number = max(numbers)
        if type(max_number) != float:
            max_number = float(max_number)
        return max_number
    except TypeError:
        return "ERROR: Invalid number!"
    except ValueError:
        return "ERROR: Invalid number!"

#print(get_max([3, -2, 1, 4]))
#print(get_max([3, -2, 'two', 4, 'one']))
#print(get_max([12, 2.5, 45, 99]))