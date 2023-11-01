def get_max_len_list(words):
    if len(words) == 1:
        return len(words[0])
    else:
        return max(len(words[0]), get_max_len_list(words[1:]))


lst = ['This', 'is', 'a', 'test']
print(get_max_len_list(lst))
lst = ['hello']
print(get_max_len_list(lst))