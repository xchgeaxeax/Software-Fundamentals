class City:
    def __init__(self, name=None, population=1, area=1):
        if area < 0:
            area = 1
        if population < 0:
            population = 1
        self.__name = name
        self.__population = population
        self.__area = area

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    def get_area(self):
        return self.__area

    def set_area(self, area):
        if area < 0:
            area = 1
        self.__area = area

    def set_name(self, name):
        self.__name = name

    def set_population(self, population):
        if population < 0:
            population = 1
        self.__population = population

    def get_population_density(self):
        return round(self.__population / self.__area, 2)

    def __str__(self):
        density = str(self.get_population_density())
        if not len(density.split('.')[1]) != 1:
            density = density + '0'
        return f"{self.__name}({density})"





city1 = City("Auckland", 1470100, 607.1)
print(city1.get_name(), city1.get_population(), city1.get_area())
city2 = City('Christchurch', 383200, 295.15)
print(city2)

city1 = City("Wellington", 215100, 112.29)
print(city1)
city2 = City('Hamilton', 176500, 110.37)
print(city2)

city2 = City('N/A')
print(city2, city2.get_population(), city2.get_area())
city2.set_name('Auckland')
city2.set_population(-1)
city2.set_area(607.10)
print(city2.get_name(), city2.get_population(), city2.get_area())
