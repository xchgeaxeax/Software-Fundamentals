"""Define a class named QuadraticEquation to represent a quadratic equation as shown below:

qe

The QuadraticEquation class contains the following:

    A private data field named __coeff_a that represents the first coefficient of an equation.
    A private data field __coeff_b that represents the second coefficient of an equation.
    A private data field __coeff_c that represents the third coefficient of an equation.
    A constructor that creates an equation with the specified coefficients or creates an equation with default values (of 1).  This method should be the special __init__(self, coeff_a = 1, coeff_b = 1, coeff_c = 1) method, or the initialiser method for the class.
    Three getter methods for all the coefficients. (i.e. get_coeff_a(self), get_coeff_b(self) and get_coeff_c(self))
"""


class QuadraticEquation:
    def __init__(self, coeff_a=1, coeff_b=1, coeff_c=1):
        self.__coeff_a = coeff_a
        self.__coeff_b = coeff_b
        self.__coeff_c = coeff_c

    def get_coeff_a(self):
        return self.__coeff_a

    def get_coeff_b(self):
        return self.__coeff_b

    def get_coeff_c(self):
        return self.__coeff_c

    def __str__(self):
        return "{}x^2 + {}x + {}".format(self.__coeff_a, self.__coeff_b, self.__coeff_c)

equation1 = QuadraticEquation(1, 2, 1)
print(equation1.get_coeff_a(), equation1.get_coeff_b(), equation1.get_coeff_c())
equation2 = QuadraticEquation()