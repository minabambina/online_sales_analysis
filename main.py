from product_manager import ProductManager
from product import Product

product_manager = ProductManager()

product1 = Product("Laptop", 1200.00, 5)
product2 = Product("Smartphone", 800.00, 10)
product3 = Product("Headphones", 150.00, 20)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)

print("Product Inventory:")
product_manager.display_all_products()

total_value = product_manager.total_inventory_value()
print(f"\nTotal Inventory Value: ${total_value:.2f}")
