class Rectangle:
    def __init__(self, width=10, height=10):  # constructor function
        self.__width = width
        self.__height = height


    def __str__(self):
        return "{} x {}".format(self.__width, self.__height)

    def get_width(self):  # accessor functions
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    # A method named __repr__(self) that returns a string that unambiguously describes the object. In this case, the __repr__ method should return a string that looks like the statement that would be used to actually create the object.
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)




r1 = Rectangle(3, 4)
print(r1)
print(repr(r1))
r2 = Rectangle()
print(r2)
print(repr(r2))