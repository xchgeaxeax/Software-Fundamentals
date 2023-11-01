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

m1 = Member(1001, "Michael")
print(m1.get_name(), m1.get_member_id())
m2 = Member(1002, "Paul")
print(m2.get_name(), m2.get_member_id())