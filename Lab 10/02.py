new_string = ""
def copy_string(word):
    global new_string
    if word:
        new_string += word[0]
        return copy_string(word[1:])
    else:
        result = new_string
        new_string = ""
        return result

s = 'hello'
print(copy_string(s))

s = 'This is a test'
print(copy_string(s))