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
        population_density = self.__population / self.__area
        return population_density

    def __str__(self):
        density = self.get_population_density()
        # density = str(self.get_population_density())
        # if not len(density.split('.')[1]) != 1:
        #     density = density + '0'
        return "{}({:.2f})".format(self.__name, density)

class Country:
    def __init__(self, country_name):
        self.__name = country_name
        self.__cities_list = []

    def add_city(self, city_name, population, area):
        new_city = City(city_name, population, area)
        self.__cities_list.append(new_city)

    def get_country_name(self):
        return self.__name

    def get_city(self, n):
        return self.__cities_list[n]

    def get_total_population(self):
        total_population = 0
        for city in self.__cities_list:
            total_population += city.get_population()
        return total_population

    def get_total_area(self):
        total_area = 0
        for city in self.__cities_list:
            total_area += city.get_area()
        return total_area



    def get_population_density(self):
        total_area = 0
        total_population = 0
        for i in range(len(self.__cities_list)):
            city = self.__cities_list[i]
            total_population += city.get_population()
            total_area += city.get_area()
            # print(city)
        return total_population / total_area
    def __str__(self):
        print(f"{self.__name}:")
        total_area = 0
        total_population = 0
        for i in range(len(self.__cities_list)):
            city = self.__cities_list[i]
            total_population += city.get_population()
            total_area += city.get_area()
            print(city)
        return "Population density = {:.2f}".format(total_population / total_area)


nz = Country("New Zealand")
nz.add_city('Auckland', 1470100, 607.10)
nz.add_city('Christchurch', 383200, 295.15)
nz.add_city('Wellington', 215100, 112.29)
nz.add_city('Hamilton', 176500, 110.37)
nz.add_city('Tauranga', 151300, 135.12)
nz.add_city('Lower Hutt', 110700, 78.52)
nz.add_city('Dunedin', 106200, 91.58)
nz.add_city('Palmerston North', 81500, 76.92)
nz.add_city('Napier', 66300, 104.90)
print("{:.2f}".format(nz.get_population_density()))
print(nz)