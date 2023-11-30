class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, left=self.__left)
            self.__left = t

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, right=self.__right)
            self.__right = t

    def insert(self, value):
        if value < self.__data:
            if self.__left is None:
                self.__left = BinarySearchTree(value)
            else:
                self.__left.insert(value)
        elif value > self.__data:
            if self.__right is None:
                self.__right = BinarySearchTree(value)
            else:
                self.__right.insert(value)
        else:
            raise ValueError('Duplicate value')

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


tree = BinarySearchTree(15)
print_tree(tree, 0)