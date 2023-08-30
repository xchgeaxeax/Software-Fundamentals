sentence = input('Enter a sentence: ')
new_sentence = ''
for i in range(len(sentence)):
    each = sentence[i]
    if each.isupper():
        new_sentence += each.lower()
        continue
    if each.islower():
        new_sentence += each.upper()
    else:
        new_sentence += each
print(new_sentence)