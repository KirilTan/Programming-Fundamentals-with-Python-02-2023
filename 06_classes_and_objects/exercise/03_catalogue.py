class Catalogue:

    def __init__(self, name_of_catalogue: str):
        self.name_of_catalogue = name_of_catalogue
        self.products = []

    def add_product(self, product_name: str):  # adds the product to the products' list
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):  # returns the catalogue info
        return_string = f"Items in the {self.name_of_catalogue} catalogue:\n"
        return_string += "\n".join(sorted(self.products))
        return return_string


# Example Usage:
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
