class Node:
   def __init__(self, data, next=None):
       self.__data = data
       self.__next = next

   def __str__(self):
       return f"{self.__data}"

   def get_data(self):
       return self.__data

   def get_next(self):
       return self.__next

   def set_data(self, new_data):
       self.__data = new_data

   def set_next(self, new_next):
       self.__next = new_next

   def add_after(self, value):
       new_node = Node(value, self.__next)
       self.__next = new_node


a_node = Node('hello')
a_node.add_after('world')
print(a_node)
print(a_node.get_next())