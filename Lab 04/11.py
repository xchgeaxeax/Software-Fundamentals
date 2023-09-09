def word_len_frequencies(sentence):
    word_freq_dict = {} # Dictionary with words as keys and their frequencies as values
    freq_words_dict = {} # Dictionary with frequencies as keys and words as values
    sentence = sentence.lower()
    word_list = sentence.split()
    for word in word_list:
        if word not in word_freq_dict:
            word_freq_dict[word] = 1
        else:
            word_freq_dict[word] += 1
    for key in word_freq_dict:
        value = word_freq_dict[key]
        if value not in freq_words_dict:
            freq_words_dict[value] = [key]
        else:
            freq_words_dict[value].append(key)
    key_list = []
    for key in freq_words_dict:
        key_list.append(int(key))
        key_list.sort(reverse=True)
    for key in key_list:

        line = str(key) + ' ' + str(sorted(freq_words_dict[key]))
        print(line)


#word_len_frequencies('the Quick BROWN fox jumps fox fox fox quick')



