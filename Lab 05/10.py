def get_phone(phones_dictionary, name):
    try:
        if type(name) != str:
            raise Exception("Invalid input!")
        elif name == '':
            raise Exception("Invalid name!")
        return phones_dictionary[name]
    except KeyError:
        return "ERROR: {} is not available.".format(name)
    except Exception as result:
        return "ERROR: {}".format(result)





phones_dictionary = {'Martin': 8202, 'Angela': 6620, 'Ann': 4947, 'Damir': 2391, 'Adriana': 7113, 'Andrew': 5654}
print(get_phone(phones_dictionary , 'Ann'))
print(get_phone(phones_dictionary , 'Daniel'))
print(get_phone(phones_dictionary , 123))
print(get_phone(phones_dictionary , ''))