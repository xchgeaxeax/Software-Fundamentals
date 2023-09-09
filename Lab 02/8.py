def build_translation_dictionary(filename):
    translation_dict = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    english_word, maori_word = line.split(':')
                    translation_dict[english_word] = maori_word
    except FileNotFoundError:
        print("File not found.")

    return translation_dict


def translate_word(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return 0


def main():
    filename = input("Enter the English to Maori dictionary filename: ")
    dictionary = build_translation_dictionary(filename)

    if dictionary:
        word = input("Enter an English word: ")
        translation = translate_word(dictionary, word)
        if translation == 0:
            print("Sorry that word doesn't exist in Maori!")
        else:
            print(f"'{word}' is translated into '{translation}'.")


if __name__ == "__main__":
    main()