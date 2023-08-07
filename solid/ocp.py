# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, price, discount):
        super().__init__(price)
        self.discount = discount

    def get_price(self):
        discounted_price = self.price * (1 - self.discount)
        return discounted_price

def calculate_total_price(products):
    total_price = sum(product.get_price() for product in products)
    return total_price

# Using the calculate_total_price function with a list of products
products = [Product(100), DiscountedProduct(50, 0.1), Product(75)]
print("Total Price:", calculate_total_price(products))
