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

    #A method named get_area(self) which will be used to calculate the area of the rectangle (the product of the width and height) and return the value.
    def get_area(self):
        return self.__width * self.__height

    # A method named get_perimeter(self) which will be used to calculate the perimeter of the rectangle (the sum of the width and height) and return the value.
    def get_perimeter(self):
        return (self.__width + self.__height) * 2



r1 = Rectangle(3, 4)
print(r1.get_area())
print(r1.get_perimeter())
r3 = Rectangle()
print(r3.get_area())
print(r3.get_perimeter())