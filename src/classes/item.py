from datetime import datetime

class Item:
    def __init__(self, item_id: int, name: str, description: str, category_id: int, selling_price: float, quantity: int, created_at: datetime, updated_at: datetime):
        self.id = item_id  # No need to specify the ID here
        self.name = name
        self.description = description
        self.category_id = category_id
        self.selling_price = selling_price
        self.quantity = quantity
        self.created_at = created_at  # Use the provided created_at value
        self.updated_at = updated_at  # Use the provided updated_at value

    def update(self):
        self.updated_at = datetime.now()  # Update the updated_at attribute with current timestamp
