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
            return "{}, {} (Available)".format(self.__title, self.__code)
        return "{}, {} (On Loan)".format(self.__title, self.__code)


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
        if len(self.__on_loan_books_list) > 0:
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
        return self.__is_on_loan == True

    def __str__(self):
        return "{}, {}, issued date={}".format(self.__member.get_name(), str(self.__book), self.__issue_date)


class MyLibrary:
    def __init__(self, filename):
        self.__books_list = []  # Book object list
        self.__on_loan_records_list = []
        result = ''
        try:
            with open(filename, "r") as file:
                for line in file:
                    book_list1 = line.strip().split(',')
                    code = book_list1[0]
                    title = book_list1[1]
                    book = Book(code, title)
                    self.__books_list.append(book)
        except FileNotFoundError:
            print(f"ERROR: The file '{filename}' does not exist.")
            return
        print(f"{len(self.__books_list)} books loaded.")

    def show_all_books(self):
        for book in self.__books_list:
            print(book)

    def find_book(self, code):
        for i in range(len(self.__books_list)):
            current_code = self.__books_list[i].get_book_code()
            if current_code == code:
                return self.__books_list[i]
            if i == len(self.__books_list):
                return None

    def borrow_book(self, book, member, issue_date):
        if book is None:
            print("ERROR: could not issue the book.")
            return
        else:
            self.__books_list.remove(book)
            title = book.get_book_title()
            current_record = Record(book, member, issue_date)
            self.__on_loan_records_list.append(current_record)
            print("{} is borrowed by {}.".format(title, member.get_name()))

    def show_available_books(self):
        for book in self.__books_list:
            if book.is_available() == True:
                print(book)



library = MyLibrary('simple_books.txt')
print()
m1 = Member(1001, "Michael")
b1 = library.find_book('QS12.02.003')
library.borrow_book(b1, m1, "2020-08-12")
print()
b2 = library.find_book('QS12.02.003') #the book is not available
library.borrow_book(b2, m1, "2020-08-12")