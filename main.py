from flask import Flask
from src.utility.db_connector import DBConnection
from src.utility.db_credentials import credentials
from src.routers.item_router import ItemRouter

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Register item routes
    app.register_blueprint(ItemRouter)

    return app

def main():
    # Example usage
    sql_file_path = 'src\\utility\\SQL\\database.sql'

    database_name = DBConnection.get_database_name_from_sql_file(sql_file_path)

    connection = DBConnection.get_instance(credentials, database_name)

    #created = DBConnection.create_database(connection, sql_file_path)

    # Create the Flask app
    app = create_app()

    # Run the Flask app
    app.run(debug=True, host='localhost', port=8080)  # Change port and host as needed

if __name__ == "__main__":
    main()
