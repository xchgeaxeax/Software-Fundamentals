def read_longest_word(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()

        longest_word = ''
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
            elif len(word) == len(longest_word) and word > longest_word:
                longest_word = word

        return longest_word


filename = input("Enter filename: ")
longest_word = read_longest_word(filename)
print(f'The longest word is "{longest_word}"')
