def get_merge_list(list_of_lists):
    # base case - when there are no more sublists left
    if len(list_of_lists) == 1:
        return list_of_lists[0]

    first = list_of_lists[0]
    second = list_of_lists[1]

    # merge two sublists into one and add it back to the main list
    merged = first + second
    result = [merged] + list_of_lists[2:]

    # call the same method again until all sublists have been combined
    return get_merge_list(result)


print(get_merge_list([[1, 2, 3], [2, 3, 5, 6], [7, 8, 9]]))