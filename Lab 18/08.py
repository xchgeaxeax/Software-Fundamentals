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

    def insert(self, new_data):
        if new_data == self.__data:
            return
        elif new_data < self.__data:
            if self.__left == None:
                self.__left = BinarySearchTree(new_data)
            else:
                self.__left.insert(new_data)
        else:
            if self.__right == None:
                self.__right = BinarySearchTree(new_data)
            else:
                self.__right.insert(new_data)

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def search(self, find_data):
        if self.__data == find_data:
            return True
        elif find_data < self.__data and self.__left != None:
            return self.__left.search(find_data)
        elif find_data > self.__data and self.__right != None:
            return self.__right.search(find_data)
        else:
            return False

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right


def print_tree(t, level):
    print(' ' * (level * 4) + str(t.get_data()))
    if t.get_left() != None:
        print('(l)', end='')
        print_tree(t.get_left(), level + 1)
    if t.get_right() != None:
        print('(r)', end='')
        print_tree(t.get_right(), level + 1)


def create_tree_from_nested_list(node_list):
    if node_list:
        result = BinarySearchTree(node_list[0])
        left = create_tree_from_nested_list(node_list[1])
        right = create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result


tree1 = create_tree_from_nested_list([7, [2, [1, None, None], [5, None, None]], [9, None, None]])
tree2 = create_tree_from_nested_list(
    [27, [14, [10, None, None], [19, None, None]], [35, [31, None, None], [42, None, None]]])
tree3 = create_tree_from_nested_list(
    [8, [3, [1, None, None], [6, [4, None, None], [7, None, None]]], [10, None, [14, [13, None, None], None]]])
tree4 = create_tree_from_nested_list(
    ['H', ['D', ['B', ['A', None, None], ['C', None, None]], ['F', ['E', None, None], ['G', None, None]]],
     ['P', ['K', ['I', None, None], ['N', None, None]], ['U', ['R', None, None], ['Y', None, None]]]])


def is_binary_search_tree(my_tree, min_value, max_value):
   """
   Check if the given binary tree is a binary search tree.

   Args:
       my_tree (BinarySearchTree): The binary tree to check.
       min_value (int): The minimum value that can be stored in the tree.
       max_value (int): The maximum value that can be stored in the tree.

   Returns:
       bool: True if the tree is a binary search tree, False otherwise.
   """

   if my_tree is None:
       return True

   if my_tree.get_data() < min_value or my_tree.get_data() > max_value:
       return False

   if my_tree.get_left() is not None and my_tree.get_left().get_data() > my_tree.get_data():
       return False

   if my_tree.get_right() is not None and my_tree.get_right().get_data() < my_tree.get_data():
       return False

   return is_binary_search_tree(my_tree.get_left(), min_value, my_tree.get_data()) and \
          is_binary_search_tree(my_tree.get_right(), my_tree.get_data(), max_value)

