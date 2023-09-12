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
    def get_discriminant(self):
        return self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c


    def has_solution(self):
        return self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c >= 0

    def get_roots(self):
        if self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c > 0:
            return (((-self.__coeff_b + math.sqrt(self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c)) / (2*self.__coeff_a)), ((-self.__coeff_b - math.sqrt(self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c)) / (2*self.__coeff_a)))
        else:
            return None

equation1 = QuadraticEquation(1, 2, 1)
print(equation1.has_solution())
equation2 = QuadraticEquation()
print(equation2.has_solution())