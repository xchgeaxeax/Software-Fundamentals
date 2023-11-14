class Node:
   def __init__(self, data, next=None):
       self.__data = data
       self.__next = next

   def __str__(self):
       # return f"Node(data={self.__data}, next={self.__next})"
       return self.__data

   def get_data(self):
       return self.__data

   def get_next(self):
       return self.__next

   def set_data(self, new_data):
       self.__data = new_data

   def set_next(self, new_next):
       self.__next = new_next



a_node = Node('hello')
print(a_node)
print(a_node.get_data())
print(a_node.get_next())