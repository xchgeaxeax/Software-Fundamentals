def get_first_mid_last(words):
    result = []
    for word in words:
        new_word = ''
        if len(word) >= 3:
            new_word += word[0]
            new_word += word[len(word) // 2]
            new_word += word[-1]
            if new_word.lower() not in result:
                result.append(new_word.lower())
    return result

def generate_words(filename):
    if filename == '':
        return "ERROR: Invalid filename!"
    try:
        with open(f'{filename}', 'r') as input_file:
            word_list = input_file.read().split()
            # print(word_list)
            result = get_first_mid_last(word_list)
            return result
    except FileNotFoundError:
        return f"ERROR: The file '{filename}' does not exist."