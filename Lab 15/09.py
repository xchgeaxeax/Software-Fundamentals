class SquareNumberIterator:
    def __init__(self, count):
        self.__current = 0
        self.__count = count

    def __next__(self):
        if self.__current < self.__count:
            result = pow(self.__current + 1, 2)
            self.__current += 1
            return result
        raise StopIteration


class SquareNumber:
    def __init__(self, count = 5):
        self.__count = count

    def __iter__(self):
        return SquareNumberIterator(self.__count)


for number in SquareNumber():
    print(number)
