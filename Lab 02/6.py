def count_consonants(word):
    word = word.lower()
    count = 0
    for char in word:
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count