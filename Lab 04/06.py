def remove_letters(word1, word2):
    result = list(word2)
    for letter in word1:
        if letter in word2:
            try:
                result.remove(letter)
            except ValueError:
                continue
    return ''.join(result)

#print(remove_letters('hello', 'world'))
