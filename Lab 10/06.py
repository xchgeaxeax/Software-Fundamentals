def get_first_lower_case(word):
    if word:
        if word[0].islower():
            return word[0]
        else:
            return get_first_lower_case(word[1:])
    else:
        return None


s = 'GREAT'
print(get_first_lower_case(s))