import copy
import types

class Stack:
    def __str__(self):
        return "Stack: " + str(self.__items)

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

    def push_list(self, a_list):
        self.__items.extend(a_list)

    def multi_pop(self, number):
        if self.__len__() < number:
            return False
        else:
            for i in range(number):
                self.pop()
            return True

    def copy(self):
        new_items = copy.deepcopy(self.__items)
        new_stack = Stack()
        new_stack.push_list(new_items)
        return new_stack

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        elif self.__len__() != other.__len__():
            return False
        else:
            for i in range(self.__len__()):
                if self.__items[i] != other.__items[i]:
                    return False
            return True


def reverse_sentence(sentence):
    """
    :param sentence: a string
    :return: a string
    """
    if not sentence:
        return ""
    else:
        stack = Stack()
        for char in sentence.split():
            if char != " ":
                stack.push(char)
            else:
                stack.push(" ")
        new_sentence = ""
        while not stack.is_empty():
            new_sentence += stack.pop() + ' '
        return new_sentence

print(reverse_sentence('hello world'))