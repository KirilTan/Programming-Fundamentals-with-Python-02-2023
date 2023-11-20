class Inventory:
    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.items = []

    def add_item(self, item: str) -> None or str:
        if self.capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self) -> int:
        return self.capacity

    def __repr__(self):
        return (f"Items: {', '.join(self.items)}."
                f"\nCapacity left: {(self.capacity - len(self.items))}")


# Example usage:
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
