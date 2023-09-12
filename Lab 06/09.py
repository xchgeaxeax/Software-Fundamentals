class Product:
    def __init__(self, product_id, product_name, product_price=1):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        return "{}(id = {}), ${}".format(
            self.__product_name, self.__product_id, self.__product_price
        )


p1 = Product(1, 'Apple iPhone SE 64GB', 799)
p2 = Product(2, 'Apple iPhone 11 64GB', 1349)
p3 = Product(3, 'Dynamix A-SC-HD15F Solder Connector')
print(p1)
print(p2)
print(p3)