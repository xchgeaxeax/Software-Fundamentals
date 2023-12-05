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

    def insert(self, element):
        self.__binary_heap.append(element)
        self.__size += 1
        self.percolate_up(self.__size)

    def get_smaller_child_index(self, index):
        if 2 * index + 1 > self.__size:
            return 2 * index
        else:
            if self.__binary_heap[2 * index] < self.__binary_heap[2 * index + 1]:
                return 2 * index
            else:
                return 2 * index + 1
