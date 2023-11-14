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
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        if not self.__items:
            raise IndexError('ERROR: The queue is empty!')
        return self.__items[len(self.__items)-1]

    def clear(self):
        self.__items = []

    def enqueue_list(self, a_list):
        for item in a_list:
            self.enqueue(item)



