word = input("Enter a word: ")
dictionary = {}

for letter in word:
    dictionary[letter] = ord(letter)

sorted_keys = sorted(dictionary.keys())

for key in sorted_keys:
    print(key + ":" + str(dictionary[key]))