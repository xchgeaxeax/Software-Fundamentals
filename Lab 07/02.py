class Book:
    global books
    books = {}
    def __init__(self, code, title):
        self.__code = code
        self.__title = title
        self.__status = True
        books.update({title:True})


    def get_book_title(self):
        return self.__title

    def get_book_code(self):
        return self.__code

    def is_available(self):
        return self.__status

    def borrow_book(self):
        self.__status = False
        books.update({self.__title:False})

    def return_book(self):
        if  self.__status:
            return
        self.__status = True
        books.update({self.__title:True})


    def __str__(self):
        if self.__status:
            status = 'Available'
        else:
            status = 'On Loan'
        return "{}, {} ({})".format(self.__title, self.__code, status)


b1 = Book("QS12.03.001", "The Lord Of The Rings")
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
b3 = Book("QS12.02.003", "The Dune Chronicles")
b1.borrow_book()
b2.borrow_book()
b3.borrow_book()
b3.return_book()
print(b1)
print(b2)
print(b3)
#print(books)