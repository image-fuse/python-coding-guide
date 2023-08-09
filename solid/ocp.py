class Product:
    def __init__(self, price: float):
        """
        Initialize a Product object.

        Parameters:
        price (float): The price of the product.

        Returns:
        None
        """
        self.price = price

    def get_price(self) -> float:
        """
        Get the price of the product.

        Returns:
        float: The price of the product.
        """
        return self.price

class DiscountedProduct(Product):
    def __init__(self, price: float, discount: float):
        """
        Initialize a DiscountedProduct object.

        Parameters:
        price (float): The original price of the product.
        discount (float): The discount percentage applied to the product.

        Returns:
        None
        """
        super().__init__(price)
        self.discount = discount

    def get_price(self) -> float:
        """
        Get the discounted price of the product.

        Returns:
        float: The discounted price of the product.
        """
        discounted_price = self.price * (1 - self.discount)
        return discounted_price

def calculate_total_price(products: list) -> float:
    """
    Calculate the total price of a list of products.

    Parameters:
    products (list): A list of Product objects.

    Returns:
    float: The total price of the products.
    """
    total_price = sum(product.get_price() for product in products)
    return total_price

# Using the calculate_total_price function with a list of products
products = [Product(100), DiscountedProduct(50, 0.1), Product(75)]
print("Total Price:", calculate_total_price(products))
