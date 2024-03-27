import bcrypt
from flask import Blueprint, request, session, jsonify, redirect
from ..components.user_crud import UserCRUD

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/login', methods=['POST'])
async def login():
    # Get username and password from request
    username = request.json.get('username')
    password = request.json.get('password')

    # Retrieve user details from the database
    user_data = await UserCRUD.read_user_by_username(username)

    if user_data:
        # Verify password
        stored_password = user_data[1]  # Assuming the password is stored in the second column
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            # Set session variables
            session['username'] = username
            session['logged_in'] = True
            session['is_admin'] = user_data[2]  # Assuming isAdmin is stored in the third column
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        return jsonify({'error': 'User not found'}), 404

@user_routes.route('/logout', methods=['GET'])
async def logout():
    # Clear session variables
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200
