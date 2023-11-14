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


def create_sample_node_chain():
    node1 = Node("nodes")
    node2 = Node("linked", node1)
    node3 = Node("three", node2)
    return node3


def print_node_chain(node_of_chain):
    while node_of_chain is not None:
        print(node_of_chain.get_data())
        node_of_chain = node_of_chain.get_next()


node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
