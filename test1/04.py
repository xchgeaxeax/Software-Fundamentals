def get_first_mid_last(words):
    result = []
    for word in words:
        new_word = ''
        if len(word) >= 3:
            new_word += word[0]

            new_word += word[len(word) // 2]
            # if len(new_word) % 2 == 0:
            #     new_word += word[len(new_word) // 2]
            # else:
            #     new_word += word[(len(new_word) ) // 2]
            new_word += word[-1]
            result.append(new_word.lower())
    return result

list1 = ["Japan", "America"]
print(get_first_mid_last(list1))