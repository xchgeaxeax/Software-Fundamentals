with open('simple_books.txt', "r") as file:
    for line in file:
        # strip string line from ,
        book_list1 = line.strip().split(',')
        print(type(book_list1))
        print(book_list1)