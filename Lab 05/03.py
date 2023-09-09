def count_consonants(word):
    no_consonants = 'aeiou'
    count = 0
    try:
        word = word.lower()
        for i in range(len(word)):
            if word[i].isalpha():
                if word[i] not in no_consonants:
                    count += 1
        return count
    except TypeError:
        return 'ERROR: Invalid input!'
    except AttributeError:
        return 'ERROR: Invalid input!'

#print(count_consonants('abcdef'))
#print(count_consonants('123'))
#print(count_consonants(123))
#print(count_consonants(''))
#print(count_consonants([123]))