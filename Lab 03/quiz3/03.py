def read_content(filename):
    file = open(filename, 'r')
    f = file.read().split('\n')
    file.close()
    return f


def get_tag_words(line):
    l = line.split(':')
    c = (l[0], sorted(l[1].split(' ')))
    return c


def create_tags_dictionary(filename):
    line = read_content(filename)
    t = {get_tag_words(each)[0]: get_tag_words(each)[1] for each in line}
    return t
