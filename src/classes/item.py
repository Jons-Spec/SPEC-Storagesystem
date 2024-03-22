class Item:
    def __init__(self, name: str, description: str, category_id: int, selling_price: float, quantity: int):
        self.id = None  # No need to specify the ID here
        self.name = name
        self.description = description
        self.category_id = category_id
        self.selling_price = selling_price
        self.quantity = quantity
