from src.utiliity.db_connector import DBConnection
from src.utiliity.db_credentials import credentials

def main():
    # Example usage
    sql_file_path = 'src\\utiliity\\SQL\\database.sql'
    database_name = DBConnection.get_database_name_from_sql_file(sql_file_path)
    if database_name:
        # Use the database name to create the DBConnection instance
        print(database_name)
    else:
        print("Database name not found in SQL file.")

if __name__ == "__main__":
    main()