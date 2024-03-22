from typing import Tuple, Optional
from ..utility.db_connector import DBConnection
from ..classes.item import Item

class ItemCRUD:
    @staticmethod
    def create_item(name: str, description: str, category_id: int, selling_price: float, quantity: int) -> bool:
        try:
            connection = DBConnection.get_instance()
            cursor = connection.cursor()

            query = "INSERT INTO Item (name, description, category_id, selling_price, quantity) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (name, description, category_id, selling_price, quantity))

            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating item: {e}")
            return False

    @staticmethod
    def read_item(item_id: int) -> Optional[Item]:
        try:
            connection = DBConnection.get_instance()
            cursor = connection.cursor()

            query = "SELECT * FROM Item WHERE id = %s"
            cursor.execute(query, (item_id,))
            item_data = cursor.fetchone()

            if item_data:
                item = Item(*item_data)
                return item
            else:
                return None
        except Exception as e:
            print(f"Error reading item: {e}")
            return None

    # Implement update_item, delete_item, and other CRUD operations similarly
        
    @staticmethod
    def update_item(item: Item) -> bool:
        try:
            connection = DBConnection.get_instance()
            cursor = connection.cursor()

            query = "UPDATE Item SET name=?, description=?, category_id=?, selling_price=?, quantity=? WHERE id=?"
            cursor.execute(query, (item.name, item.description, item.category_id, item.selling_price, item.quantity, item.id))

            connection.commit()  # Commit the changes to the database
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating item: {e}")
            return False
        
    @staticmethod
    def delete_item(item_id: int) -> Optional[Item]:
        try:
            connection = DBConnection.get_instance()
            cursor = connection.cursor()

            query = "DELETE FROM Item WHERE id = %s"
            cursor.execute(query, (item_id,))
            connection.commit()

            # Check if any rows were affected
            if cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error deleting item: {e}")
            return None
