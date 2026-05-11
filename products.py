from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):

        if value < 0:
            print("Invalid price")

        else:
            self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):

        if value < 0:
            print("Invalid stock")

        else:
            self._stock = value

    @abstractmethod
    def apply_discount(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, stock, shipping_cost):

        super().__init__(product_id, name, price, stock)

        self.shipping_cost = shipping_cost

    def apply_discount(self):

        discounted_price = self.price * 0.9

        return discounted_price + self.shipping_cost

    def display_info(self):

        print(f"""
ID: {self.product_id}
Name: {self.name}
Price: {self.price}
Stock: {self.stock}
Shipping Cost: {self.shipping_cost}
Type: Physical Product
""")


class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, file_size):

        super().__init__(product_id, name, price, stock)

        self.file_size = file_size

    def apply_discount(self):

        return self.price * 0.8

    def display_info(self):

        print(f"""
ID: {self.product_id}
Name: {self.name}
Price: {self.price}
Stock: {self.stock}
File Size: {self.file_size}
Type: Digital Product
""")