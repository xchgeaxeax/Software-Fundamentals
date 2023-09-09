def get_word_tag_tuple(tags_dictionary, search_word):
    for i in tags_dictionary:
        if search_word in tags_dictionary[i]:
            key = i
    return search_word, key


def get_tag_tuple_list(tags_dictionary, sentence):
    l = sorted(set([get_word_tag_tuple(tags_dictionary, i) for i in sentence.lower().split(' ')]))
    return l









