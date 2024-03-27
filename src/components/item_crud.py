from typing import List, Tuple, Optional
from ..utility.db_connector import DBConnection
from ..classes.item import Item
from ..utility.db_credentials import credentials
from datetime import datetime

class ItemCRUD:

    @staticmethod
    def get_all_items() -> List[Tuple[int, str, str, int, float, int]]:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            query = "SELECT * FROM Item"
            cursor.execute(query)
            items = cursor.fetchall()

            cursor.close()
            return items
        except Exception as e:
            print(f"Error fetching items: {e}")
            return []

    @staticmethod
    def create_item(name: str, description: str, category_id: int, selling_price: float, quantity: int) -> bool:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()
            creation_date = datetime.now()

            query = "INSERT INTO Item (name, description, category_id, selling_price, quantity, created_at) VALUES (%s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (name, description, category_id, selling_price, quantity, creation_date))

            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating item: {e}")
            return False

    @staticmethod
    def read_item(item_id: int) -> Optional[Item]:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            query = "SELECT * FROM Item WHERE item_id = %s"
            cursor.execute(query, (item_id,))
            item_data = cursor.fetchone()

            if item_data:
                return item_data
            else:
                return None
        except Exception as e:
            print(f"Error reading item: {e}")
            return None

    @staticmethod
    def get_items_by_category(category_id: int) -> List[Tuple[int, str, str, int, float, int]]:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            query = "SELECT * FROM Item WHERE category_id = %s"
            cursor.execute(query, (category_id,))
            items = cursor.fetchall()

            cursor.close()
            return items
        except Exception as e:
            print(f"Error fetching items by category: {e}")
            return []
        
    @staticmethod
    def update_item(item: Item) -> bool:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()
            item.update()

            query = "UPDATE Item SET name=%s, description=%s, category_id=%s, selling_price=%s, quantity=%s, updated_at=%s WHERE item_id=%s"
            cursor.execute(query, (item.name, item.description, item.category_id, item.selling_price, item.quantity, item.updated_at, item.id))

            connection.commit()  # Commit the changes to the database
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating item: {e}")
            return False
        
    @staticmethod
    def delete_item(item_id: int) -> Optional[Item]:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            query = "DELETE FROM Item WHERE item_id = %s"
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
