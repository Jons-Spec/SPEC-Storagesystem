from src.utiliity.db_connector import DBConnection
from src.utiliity.db_credentials import credentials

def main():
    # Example usage
    sql_file_path = 'src\\utiliity\\SQL\\database.sql'

    database_name = DBConnection.get_database_name_from_sql_file(sql_file_path)

    connection = DBConnection.get_instance(credentials)

    created = DBConnection.create_database(connection, sql_file_path)


if __name__ == "__main__":
    main()
