from typing import List, Tuple
from ..utility.db_connector import DBConnection

class CategoryCRUD:
    @staticmethod
    def create_category(name: str, description: str) -> bool:
        # Similar to ItemCRUD
        pass

    @staticmethod
    def read_category(category_id: int) -> Tuple[int, str, str]:
        # Similar to ItemCRUD
        pass

    # Implement update_category, delete_category, and other CRUD operations similarly
