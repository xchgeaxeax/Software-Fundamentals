def create_dictionary(sentence):
    word_lists = {}

    # Split the sentence into words
    words = sentence.lower().split()

    # Iterate over the words and add them to the respective key in the dictionary
    for word in words:
        length = len(word)
        if length not in word_lists:
            word_lists[length] = []
        if word not in word_lists[length]:
            word_lists[length].append(word)

    # Sort the word lists in alphabetical order
    for key in word_lists:
        word_lists[key].sort()
        #print(word_lists[key])

    return word_lists


# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Create the dictionary
result = create_dictionary(sentence)

# Print the contents of the dictionary
for i in sorted(result):
    print(i, end=' ')
    str1 = ''
    for j in result[i]:
        str1 += (j + ' ')
    print(str1[:len(str1) - 1])