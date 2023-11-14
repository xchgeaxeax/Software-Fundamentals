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


class LinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        current_node = self.__head
        result = "["
        while current_node is not None:
            result += str(current_node)
            if current_node.get_next() is not None:
                result += ", "
            current_node = current_node.get_next()
        return result + ']'

    def add(self, value):
        new_node = Node(value, self.__head)
        self.__head = new_node

    def size(self):
        count = 0
        current_node = self.__head
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def get_head(self):
        return self.__head

    def clear(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def __len__(self):
        return self.size()

    def __contains__(self, search_value):
        current_node = self.__head
        while current_node is not None:
            if current_node.get_data() == search_value:
                return True
            current_node = current_node.get_next()
        return False

    def __getitem__(self, index):
        current_node = self.__head
        for i in range(index):
            current_node = current_node.get_next()
        try:
            return current_node.get_data()
        except AttributeError:
            raise StopIteration

    def add_all(self, a_list):
        for item in a_list:
            self.add(item)

    def get_min_odd(self):
        min_odd = 999
        current_node = self.__head
        while current_node is not None:
            if current_node.get_data() % 2 == 1 and current_node.get_data() < min_odd:
                min_odd = current_node.get_data()
            current_node = current_node.get_next()
        return min_odd

    def reverse(self):
        current_node = self.__head
        prev_node = None
        while current_node is not None:
            next_node = current_node.get_next()
            current_node.set_next(prev_node)
            prev_node = current_node
            current_node = next_node
        self.__head = prev_node


class LinkedListIterator:
    def __init__(self, head):
        self.__current = head
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter >= len(self.__current):
            raise StopIteration
        else:

            current_element = self.__current[self.__counter].get_data()
            self.__counter += 1
            return current_element



values = LinkedList()
values.add('cherry')
values.add('banana')
values.add('apple')
for value in values:
    print(value)

values = LinkedList()
values.add(1)
values.add(2)
values.add(3)
for value in values:
    print(value)
