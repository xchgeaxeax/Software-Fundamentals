import math

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

    def get_discriminant(self):
        return self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c


    def has_solution(self):
        return self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c >= 0

    def get_root1(self):
        if self.has_solution():
            return (-self.__coeff_b + math.sqrt(self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c)) / (2*self.__coeff_a)
        else:
            return None

    def get_root2(self):
        if self.has_solution():
            return (-self.__coeff_b - math.sqrt(self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c)) / (2*self.__coeff_a)
        else:
            return None
    def __str__(self):
        if not self.has_solution():
            return "The equation has no roots."
        elif self.get_root1() != self.get_root2():
            return "The roots are %.2f and %.2f." % (self.get_root1(), self.get_root2())
        else:
            return "The root is %.2f." % (self.get_root1())


equation1 = QuadraticEquation(4, 4, 1)
print(equation1)
equation2 = QuadraticEquation()
print(equation2)
equation3 = QuadraticEquation(1, 2, -63)
print(equation3)
