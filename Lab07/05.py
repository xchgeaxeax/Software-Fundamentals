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
        return self.__status == True
    def return_book(self):
        self.__status = True
    def borrow_book(self):
        self.__status = False
    def __str__(self):
        if self.__status:
            return "{}, {} (Available)".format(self.__title,self.__code)
        return "{}, {} (On Loan)".format(self.__title,self.__code)

class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__on_loan_books_list = []
    def borrow_book(self, book):
        self.__on_loan_books_list.append(book)
    def __str__(self):
        result = self.__name
        result += "\nOn loan book(s):\n"
        if len(self.__on_loan_books_list)>0:
            lines = "\n".join([str(b.get_book_title()) for b in self.__on_loan_books_list])
            result += lines
        else:
            result += "-"
        return result
    def get_name(self):
        return self.__name
    def get_member_id(self):
        return self.__member_id
    def get_on_loan_books(self):
        return self.__on_loan_books_list
    def return_book(self, the_book):
        self.__on_loan_books_list.remove(the_book)



class Record:
    def __init__(self, book, member, issue_date):
        self.__book = book
        self.__member = member
        self.__is_on_loan = True
        self.__issue_date = issue_date
        self.__book.borrow_book()
        self.__member.borrow_book(book)
    def return_book(self):
        self.__is_on_loan = False
        self.__book.return_book()
        self.__member.return_book(self.__book)
    def get_book_code(self):
        return self.__book.get_book_code()
    def get_member_id(self):
        return self.__member.get_member_id()
    def get_issue_date(self):
        return self.__issue_date
    def is_on_loan(self):
        return self.__is_on_loan== True
    def __str__(self):
        return "{}, {}, issued date={}".format(self.__member.get_name(), str(self.__book), self.__issue_date)






m1 = Member(1001, "Michael")
b1 = Book("QS12.03.001","The Lord Of The Rings")
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
b3 = Book("QS12.02.003", "The Dune Chronicles")
r1 = Record(b1, m1, "2020-08-12")
list9 = ['QS12.01.005','The Foundation Trilogy']
b9 = Book(list9[0], list9[1])

print(r1.get_member_id(), r1.get_book_code(), r1.get_issue_date(), r1.is_on_loan())
print()
print(m1)
print()
print(b1)
print(globals())