class Product:
    def __init__(self, product_id, product_name, product_price=1):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        return "{}(id = {}), ${}".format(
            self.__product_name, self.__product_id, self.__product_price
        )

    def set_product_price(self, product_price):
        if product_price < 0:
            return None
        self.__product_price = product_price

    def get_product_price(self):
        return self.__product_price
    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def get_product_id(self):
        return self.__product_id
    def set_product_id(self, product_id):
        if product_id <= 0:
            return None
        self.__product_id = product_id


p1 = Product(1, 'Apple iPhone SE 64GB', 799)
print(p1.get_product_price())
print(p1.get_product_name())
print(p1.get_product_id())
p1.set_product_price(-10)
p1.set_product_name("Unknown")
p1.set_product_id(10)
print(p1)