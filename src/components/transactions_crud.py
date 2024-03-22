from typing import List, Tuple
from ..utility.db_connector import DBConnection

class TransactionCRUD:
    @staticmethod
    def create_transaction(item_id: int, quantity: int, transaction_type: str, transaction_date: str, profit: float) -> bool:
        # Similar to ItemCRUD
        pass

    @staticmethod
    def read_transaction(transaction_id: int) -> Tuple[int, int, int, str, str, float]:
        # Similar to ItemCRUD
        pass

    # Implement update_transaction, delete_transaction, and other CRUD operations similarly
