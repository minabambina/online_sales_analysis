from product_manager import ProductManager
from product import Product
from cart import Cart

product_manager = ProductManager()

product1 = Product("Mouse", 1200.00, 5)
product2 = Product("Smartphone", 800.00, 7)
product3 = Product("TV", 150.00, 5)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)

print("Product Inventory:")
product_manager.display_all_products()

total_value = product_manager.total_inventory_value()
print(f"\nTotal Inventory Value: ${total_value:.2f}")

cart = Cart()

cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

cart.display_cart_contents()

cart_total = cart.total_cart_value()
print(f"\nTotal value of the cart: ${cart_total:.2f}")
