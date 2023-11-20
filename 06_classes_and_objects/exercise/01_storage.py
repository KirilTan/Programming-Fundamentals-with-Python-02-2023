class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):  # adds the product in the storage if there is enough space for it
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(product)

    def get_products(self):  # returns the storage list
        return Storage.storage

