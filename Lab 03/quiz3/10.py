import random


def print_random_phrase(tags_dictionary):
    print(tags_dictionary['DT'][random.randrange(len(tags_dictionary['DT']))],
          tags_dictionary['JJ'][random.randrange(len(tags_dictionary['JJ']))],
          tags_dictionary['NN'][random.randrange(len(tags_dictionary['NN']))])
