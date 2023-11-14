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


def create_node_chain(values):
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.set_next(Node(value))
        current = current.get_next()
    return head


def convert_to_list(first_node):
    elements = []
    current_node = first_node
    while current_node is not None:
        elements.append(current_node.get_data())
        current_node = current_node.get_next()
    return elements

def get_consecutive_sum(first_node):
    result = []
    current_node = first_node
    while current_node is not None:
        sum = 0
        temp = current_node
        while temp is not None:
            sum += temp.get_data()
            temp = temp.get_next()
        result.append(sum)
        current_node = current_node.get_next()
    return result


node1 = Node(5)
node2 = Node(10, node1)
node3 = Node(30, node2)
node4 = Node(40, node3)
print(get_consecutive_sum(node4))