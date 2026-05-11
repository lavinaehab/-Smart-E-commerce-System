class ShoppingCart:

    def __init__(self):

        self.items = []

    def add_product(self, product):

        self.items.append(product)

        print(f"{product.name} added to cart")

    def view_cart(self):

        if len(self.items) == 0:

            print("Cart is empty")

        else:

            print("\nCart Items:\n")

            for item in self.items:

                item.display_info()

    def checkout(self):

        if len(self.items) == 0:

            print("Cart is empty")
            return

        total = 0

        print("\nCheckout Details:\n")

        for item in self.items:

            final_price = item.apply_discount()

            print(f"{item.name} Final Price = {final_price}")

            total += final_price

        print(f"\nTotal Price = {total}")