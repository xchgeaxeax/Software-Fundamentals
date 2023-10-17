def modify_list(data1):
    global data
    result = []
    for i in range(len(data1)):
        # result.append(data[i][i+1:])
        str1 = data1[i]
        str2 = str1[i + 1:]
        result.append(str2)

    data = result
    return result


data = ["bushes", "and", "shrubs", "trees"]
modify_list(data)
print(data)