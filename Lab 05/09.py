def get_maori_word(dictionary, word):
    try:
        return dictionary[word]
    except KeyError:
        return "ERROR: {} is not available.".format(word)




#dictionary = {'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
#              'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
#              'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
#print(get_maori_word(dictionary, 'house'))
#print(get_maori_word(dictionary, 'orange'))
#print(get_maori_word(dictionary, 'tooth'))