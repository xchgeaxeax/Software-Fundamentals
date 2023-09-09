def print_keys_values_inorder(dictionary):
    keys = sorted(dictionary.keys())
    for key in keys:
        values = sorted(dictionary[key])
        words = " ".join(values)
        print(key, words)