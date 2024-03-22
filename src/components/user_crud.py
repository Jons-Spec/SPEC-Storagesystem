from typing import Tuple, Optional
from bcrypt import hashpw, gensalt, checkpw
from ..utility.db_connector import DBConnection
from ..utility.db_credentials import credentials

class UserCRUD:
    @staticmethod
    def create_user(username: str, password: str, isAdmin: bool) -> bool:
        try:
            # Hash the password
            hashed_password = hashpw(password.encode('utf-8'), gensalt())

            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            # Insert user data into the database
            query = "INSERT INTO User (username, password, is_admin) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, hashed_password, isAdmin))

            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    @staticmethod
    def read_user(user_id: int) -> Tuple[int, str, bool]:
        # Implementation remains the same
        pass

    # Implement update_user, delete_user, and other CRUD operations similarly

    @staticmethod
    def authenticate_user(username: str, password: str) -> Optional[bool]:
        try:
            connection = DBConnection.get_instance()
            cursor = connection.cursor()

            # Retrieve hashed password from the database
            query = "SELECT password FROM User WHERE username = %s"
            cursor.execute(query, (username,))
            user_data = cursor.fetchone()

            if user_data:
                hashed_password = user_data[0]

                # Check if the entered password matches the hashed password
                if checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                    return True
                else:
                    return False
            else:
                return None
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None
