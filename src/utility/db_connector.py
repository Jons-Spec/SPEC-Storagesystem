from typing import Dict
import mysql.connector as mysql

class DBConnection:
    __instance = None
    sql_file_path = 'src\\utility\\SQL\\database.sql'

    def __init__(self, host: str, username: str, password: str, port: str, database: str) -> None:
        self.host = host
        self.user = username
        self.password = password
        self.port = port
        self.database = database
        
        if DBConnection.__instance is None:
            DBConnection.__instance = mysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, database=self.database)
            if not self.database:
                self.create_database()
        else:
            raise Exception("Can't create another MySQL connection")
        
    def create_database(self, sql_file_path) -> bool:
        cursor = DBConnection.__instance.cursor()

        with open(sql_file_path, 'r') as sql_file:
            sql_commands = sql_file.read().split(';')

        for command in sql_commands:
            if command.strip():
                cursor.execute(command)

        cursor.close()
        print("Database created successfully.")
        return True

    @staticmethod
    def get_database_name_from_sql_file() -> str:
        with open(DBConnection.sql_file_path, 'r') as sql_file:
            for line in sql_file:
                if line.strip().startswith('USE'):
                    parts = line.strip().split(' ')
                    return parts[1].strip('`;')  # Extracting the database name from the USE statement
        return None  # Database name not found

    @staticmethod
    def get_instance(credentials: Dict[str, str]) -> object:
        if not DBConnection.__instance:
            database_name = DBConnection.get_database_name_from_sql_file()
            return DBConnection(credentials['DB_HOST'], credentials['DB_USER'], credentials['DB_PASS'], credentials['DB_PORT'], database_name)
        return DBConnection.__instance
    
    @staticmethod
    def close_instance() -> None:
        if DBConnection.__instance:
            DBConnection.__instance.close()
            DBConnection.__instance = None
