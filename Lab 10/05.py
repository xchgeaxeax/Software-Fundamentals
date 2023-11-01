# Write a recursive function named count_consonants(word) that takes a string as a parameter and returns the number of consonants (i.e. letters: bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ) in the parameter string. The function should return 0 if there are no consonants in the parameter string.


def count_consonants(word):
    if len(word) == 0:
        return 0
    elif word[0] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        return 1 + count_consonants(word[1:])
    else:
        return count_consonants(word[1:])


print(count_consonants('This is a Test'))