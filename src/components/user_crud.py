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
    def read_user_by_username(username: str) -> Optional[Tuple[str, str, bool]]:
        try:
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            # Retrieve user data from the database based on username
            query = "SELECT username, password, is_admin FROM User WHERE username = %s"
            cursor.execute(query, (username,))
            user_data = cursor.fetchone()

            cursor.close()

            if user_data:
                return user_data
            else:
                return None
        except Exception as e:
            print(f"Error reading user: {e}")
            return None
        
    @staticmethod
    def update_user(username: str, password: str, isAdmin: bool, search_name: str) -> bool:
        try:
            # Hash the password
            hashed_password = hashpw(password.encode('utf-8'), gensalt())
            connection = DBConnection.get_instance(credentials)
            cursor = connection.cursor()

            query = "UPDATE User SET username=%s, password=%s, is_admin=%s WHERE username=%s"
            cursor.execute(query, (username, hashed_password, isAdmin, search_name))

            connection.commit()  # Commit the changes to the database
            cursor.close()
            return True  # Placeholder success response
        except Exception as e:
            print(f"Error updating user: {e}")
            return None
            
    # Maybe not needed
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
