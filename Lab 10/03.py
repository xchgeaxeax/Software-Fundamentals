def reverse_string(word):
    if word:
        return word[-1] + reverse_string(word[:-1])
    return ""
s = 'hello'
print(reverse_string(s))