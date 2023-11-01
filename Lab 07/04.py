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

    def borrow_book(self):
        self.__status = False

    def return_book(self):
        if  self.__status:
            return
        self.__status = True

    def __str__(self):
        if self.__status:
            status = 'Available'
        else:
            status = 'On Loan'
        return "{}, {} ({})".format(self.__title, self.__code, status)
class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__on_loan_books_list = []

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list
    # A method named borrow_book(self, book) which takes a Book object as a parameter and adds the book to the on loan books list.
    def borrow_book(self, book):
        self.__on_loan_books_list.append(str(book).split(',')[0])
        #result = str(book)
        #print(result.split(',')[0])

    def return_book(self, book):
        self.__on_loan_books_list.remove(str(book).split(',')[0])
    # A __str__ method that returns a string representation of the object formatted as in the examples below.
    def __str__(self):
        result = '{}\nOn loan book(s):\n'
        if self.__on_loan_books_list == []:
            result += '-'
        else:
            for book in self.__on_loan_books_list:
                result += '{}\n'.format(book)
            result = result[:-1]
        return result.format(self.__name)
        #return "{0}".format(self.__name)



m1 = Member(1001, "Michael")
m2 = Member(1002, "Paul")
b1 = Book("QS12.03.001","The Lord Of The Rings")
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
b3 = Book("QS12.02.003", "The Dune Chronicles")
m1.borrow_book(b1)
m1.borrow_book(b2)
m1.borrow_book(b3)
m1.return_book(b1)
print(m1)
print()
print(m2)