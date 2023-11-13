class Stack:
    def __str__(self):
        return "Stack: " + str(self.__items)
        # return "".join([str(item) for item in self.__items])

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items.pop()

    def peek(self):
        if not self.__items:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items[len(self.__items) - 1]
