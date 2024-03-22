from flask import Flask
from src.utility.db_connector import DBConnection
from src.utility.db_credentials import credentials
from src.routers.item_router import item_routes
from src.routers.user_router import user_routes
from src.components.user_crud import UserCRUD



def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Register item routes
    app.register_blueprint(item_routes)

    # Register user routes
    app.register_blueprint(user_routes)

    # Set secret key for session management
    app.secret_key = 'your_secret_key'

    return app

def main():
    # Example usage
    connection = DBConnection.get_instance(credentials)
    if connection:
        print("Connection to databse created")
    else:
        print("No database connection")

    #created = DBConnection.create_database(connection, sql_file_path)
        
    #test admin user for later    
    admin_user = UserCRUD.create_user("adminuser","admin123",True)
    if admin_user:
        print("user created")
    else:
        print("user already exsists")
    # Create the Flask app
    app = create_app()

    # Run the Flask app
    app.run(debug=True, host='localhost', port=8080)  # Change port and host as needed

if __name__ == "__main__":
    main()
