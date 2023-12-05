class PriorityQueue:
    def __init__(self):
        self.__binary_heap = [0]
        self.__size = 0

    def __str__(self):
        return str(self.__binary_heap)

    def __len__(self):
        return self.__size

    def add_all(self, a_list):
        for item in a_list:
            self.__binary_heap.append(item)
            self.__size += 1


pq = PriorityQueue()
pq.add_all([5, 8, 7, 9, 10])
print(pq)
print(len(pq))
