from products import PhysicalProduct, DigitalProduct
from cart import ShoppingCart


products = [

    PhysicalProduct(1, "Laptop", 30000, 5, 100),

    PhysicalProduct(2, "Keyboard", 1000, 10, 50),

    DigitalProduct(3, "Python Course", 500, 20, "5GB"),

    DigitalProduct(4, "Ebook", 200, 15, "20MB")
]


cart = ShoppingCart()


while True:

    print("""
========= SMART E-COMMERCE =========

1. View Products
2. Add Product To Cart
3. View Cart
4. Checkout
5. Exit
""")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("\nAvailable Products:\n")

            for product in products:

                product.display_info()

        elif choice == 2:

            product_id = int(input("Enter Product ID: "))

            found = False

            for product in products:

                if product.product_id == product_id:

                    cart.add_product(product)

                    found = True

                    break

            if not found:

                print("Product not found")

        elif choice == 3:

            cart.view_cart()

        elif choice == 4:

            cart.checkout()

        elif choice == 5:

            print("Exiting system...")

            break

        else:

            print("Invalid choice")

    except ValueError:

        print("Please enter numbers only")