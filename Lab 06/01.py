class Rectangle:
    def __init__(self, width=10, height=10):  # constructor function
        self.__width = width
        self.__height = height

    def get_width(self):  # accessor functions
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height




r1 = Rectangle(3, 4)
print(r1.get_width(), r1.get_height())
r2 = Rectangle()
print(r2.get_width(), r2.get_height())