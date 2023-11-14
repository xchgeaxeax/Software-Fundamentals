import copy
import types


class Queue:
    def __init__(self):
        self.__items = []

    def __str__(self):
        return "Queue: " + str(self.__items)

    def __len__(self):
        return len(self.__items)

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if not self.__items:
            raise IndexError('ERROR: The queue is empty!')
        return self.__items.pop(0)

    def size(self):
        return len(self.__items)

    def peek(self):
        if not self.__items:
            raise IndexError('ERROR: The queue is empty!')
        return self.__items[len(self.__items) - 1]

    def clear(self):
        self.__items = []

    def enqueue_list(self, a_list):
        for item in a_list:
            self.enqueue(item)

    def multi_dequeue(self, number):
        if number > len(self.__items):
            return False
        else:
            dequeued_list = []
            for i in range(number):
                dequeued_list.append(self.dequeue())
            return True


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


def mirror_queue(a_queue):
    a_list = []
    result = []
    while not a_queue.is_empty() :
        a_list.append(a_queue.dequeue())
    for i in range(len(a_list)):
        result.insert(-i,a_list[i])
        result.insert(i, a_list[i])
    for i in result:
        a_queue.enqueue(i)



q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1)
mirror_queue(q1)
print(q1)
