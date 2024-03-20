from typing import Dict
import mysql.connector as mysql

class DBConnection:
    
    __instance = None

    def __init__(self, host: str, username: str, password: str, port: str) -> None:
        self.host = host
        self.user = username
        self.password = password
        self.port = port
        self.database = None
        
        if DBConnection.__instance is None:
            DBConnection.__instance = mysql.connect(host=self.host, user=self.user, password=self.password, port=self.port)
            if self.database:
                self.create_database(self.database)
        else:
            raise Exception("Can't create another MySQL connection")
        
    def create_database(self, sql_file_path: str) -> None:
        cursor = DBConnection.__instance.cursor()
        
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()

        cursor.execute(sql_script, multi=True)
        cursor.close()
    
    def get_database_name_from_sql_file(sql_file_path: str) -> str:
        with open(sql_file_path, 'r') as sql_file:
            for line in sql_file:
                if line.strip().startswith('USE'):
                    parts = line.strip().split(' ')
                    return parts[1].strip('`;')  # Extracting the database name from the USE statement
        return None  # Database name not found


    @staticmethod
    def get_instance(credantials: Dict[str, str]) -> object:
        if not DBConnection.__instance:
            DBConnection(credantials['DB_HOST'], credantials['DB_USER'], credantials['DB_PASS'], credantials['DB_PORT'])
        return DBConnection.__instance
    
    @staticmethod
    def close_instance() -> None:
        DBConnection.__instance.close()

