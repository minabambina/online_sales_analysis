class Cart:
    def __init__(self):
        self.cart_items = []  # List to hold the products in the cart

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Added {product.name} to the cart.")

    def total_cart_value(self):
        total_value = sum(item.price * item.quantity for item in self.cart_items)
        return total_value

    def display_cart_contents(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart_items:
                item.display_info()
