from typing import List, Tuple
from ..utility.db_connector import DBConnection

class UserCRUD:
    @staticmethod
    def create_user(username: str, password: str, email: str) -> bool:
        # Similar to ItemCRUD
        pass

    @staticmethod
    def read_user(user_id: int) -> Tuple[int, str, str]:
        # Similar to ItemCRUD
        pass

    # Implement update_user, delete_user, and other CRUD operations similarly
