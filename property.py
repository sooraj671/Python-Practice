class Product:
    
    def __init__(self, price):
        self.price = price
    
    @property    
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 0 :
            raise ValueError("Price cannot be negative.")
        self.__price = price
    
    # price = property(get_price, set_price)
    
product = Product(10)
product.price =20
print(product.price)