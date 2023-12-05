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

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.__binary_heap[index] < self.__binary_heap[index // 2]:
                self.__binary_heap[index // 2], self.__binary_heap[index] = self.__binary_heap[index], \
                    self.__binary_heap[index // 2]
            index = index // 2


pq = PriorityQueue()
pq.add_all([11, 9, 5])
pq.percolate_up(3)
print(pq)
print(len(pq))

print()

pq = PriorityQueue()
pq.add_all([6, 7, 8, 9, 22, 45, 1])
pq.percolate_up(7)
print(pq)
