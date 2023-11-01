class Book:
    def __init__(self, code, title):
        self.__code = code
        self.__title = title
        self.__status = True

    def get_book_title(self):
        return self.__title

    def get_book_code(self):
        return self.__code

    def is_available(self):
        return self.__status


b1 = Book("QS12.03.001", "The Lord Of The Rings")
print(b1.get_book_code(), b1.get_book_title(), b1.is_available())
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
print(b2.get_book_code(), b2.get_book_title(), b2.is_available())