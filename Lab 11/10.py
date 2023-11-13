def binary_search(values, item):
    harf_len = len(values) // 2
    if len(values) == 0:
        return False
    else:
        print(values[:harf_len], values[harf_len], values[harf_len+1:])
        if values[harf_len] == item:
            return True
        elif values[harf_len] > item:
            return binary_search(values[:harf_len], item)
        else:
            return binary_search(values[harf_len+1:], item)


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))