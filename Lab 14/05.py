class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def __str__(self):
        return f"{self.__data}"

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

    def add_after(self, value):
        new_node = Node(value, self.__next)
        self.__next = new_node

    def remove_after(self):
        if self.__next is not None:
            self.__next = self.__next.__next

    def __contains__(self, value):
        if self.__data == value:
            return True
        elif self.__next is not None:
            return value in self.__next
        else:
            return False

    def get_sum(self):
        total = self.__data
        if self.__next is not None:
            total += self.__next.get_sum()
        return total


node1 = Node(5)
node2 = Node(10, node1)
node3 = Node(30, node2)
node4 = Node(40, node3)
print(node1.get_sum())
print(node4.get_sum())