class CircularQueue:
    def __init__(self, size=8):
        self.__items = [None] * size
        self.__front = 0
        self.__back = size - 1
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def enqueue(self, element):
        if self.__is_full():
            raise IndexError("ERROR: The queue is full.")

        self.__back += 1
        if self.__back == len(self.__items):
            self.__back = 0
        self.__items[self.__back % len(self.__items)] = element
        self.__count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")

        retval = self.__items[self.__front]
        # self.__items[self.__front] = None
        self.__front += 1
        if self.__front == len(self.__items):
            self.__front = 0
        self.__count -= 1
        return retval

    def peek(self):
        if self.__is_empty():
            raise IndexError("ERROR: The queue is empty.")
        return self.__items[self.__front]

    def clear(self):
        for i in range(len(self.__items)):
            self.__items[i] = None

        self.__front = 0
        self.__back = len(self.__items) - 1
        self.__count = 0

    def __repr__(self):
        return f"{type(self).__name__}(size={len(self.__items)})"

    def __str__(self):
        result = ""
        current = self.__front
        # while current != (self.__back + 1) % len(self.__items):
        #     result += str(self.__items[current]) + ", "
        #     current = (current + 1) % len(self.__items)
        # for i in range(self.__front, self.__back + 1):
        for i in range(len(self.__items)):
            if self.__items[i] is None:
                result += "None, "
            else:
                result += str(self.__items[i]) + ", "

        return f"[{result[:-2]}], front:{self.__front}, back:{self.__back}, count:{self.count}"

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def is_full(self):
        for i in self.__items:
            if i == None:
                return False
        else:
            return True


    def __is_full(self):
        return self.__count == len(self.__items)

    def print_all(self):
        if self.__front > self.__back:
            new_count = self.count
            if self.__front + self.count > len(self.__items):
                for i in range(self.__front, len(self.__items)):
                    print(self.__items[i], end=' ')
                    new_count -= 1
                for i in range(0, new_count):
                    print(self.__items[i], end=' ')
        else:
            for i in range(self.__front, self.__back + 1):
                print(self.__items[i], end=' ')
        print()


q1 = CircularQueue(4)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.print_all()
print(q1.dequeue())
q1.print_all()