def get_tags_frequency(list_of_tuples):
    dic = {}
    for i in list_of_tuples:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    return dic










