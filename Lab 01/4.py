# Function to check if two words are anagrams
def check_anagrams(word1, word2):
    # Convert both words to lowercase and remove any whitespace
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Sort the characters in both words
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    # Compare the sorted words
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False


# Prompt the user to enter two words
word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

# Check if the words are anagrams and print the result
if check_anagrams(word1, word2):
    print(word1 + " and " + word2 + " are anagrams of each other.")
else:
    print(word1 + " and " + word2 + " are not anagrams of each other.")