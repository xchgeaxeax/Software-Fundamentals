import re

def palindrome_filter(sentence):
    sentence = sentence.lower()
    filtered = re.sub('[^a-z]+', '', sentence)
    return filtered


def is_palindrome(sentence):
    if len(sentence) <= 1:
        return True
    else:
        length = len(sentence) // 2
        left = sentence[:length]
        right = sentence[-length:]

    # Base case: If we've reached the middle of the word, it's a palindrome
        if not right:
            return True

    # Recursive case: Check that both sides match at each step
        else:
            return left == right[-1::-1] or (is_palindrome(left) and False)



print(palindrome_filter("Able was I ere I saw Elba."))
print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))
print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))
print(is_palindrome(palindrome_filter("Ebla was I ere I saw Elba.")))
print(is_palindrome("a"))
print(len('ablewasiereisawelba'))
