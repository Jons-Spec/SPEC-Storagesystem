from flask import Blueprint, request, jsonify
from ..components.item_crud import ItemCRUD

item_routes = Blueprint('item_routes', __name__)

@item_routes.route('/items', methods=['POST'])
def create_item():
    data = request.json
    success = ItemCRUD.create_item(**data)
    if success:
        return jsonify({"message": "Item created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create item"}), 500

@item_routes.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id: int):
    item_from_db = ItemCRUD.read_item(item_id)
    item = {
        "id": item_from_db[0],
        "name": item_from_db[1],
        "description": item_from_db[2],
        "category_id": item_from_db[3],
        "selling_price": item_from_db[4],
        "quantity": item_from_db[5],
        "created at": item_from_db[6],
        "updated at": item_from_db[7]
        }
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@item_routes.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id: int):
    data = request.json
    success = ItemCRUD.update_item(item_id, **data)
    if success:
        return jsonify({"message": "Item updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update item"}), 500

@item_routes.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id: int):
    success = ItemCRUD.delete_item(item_id)
    if success:
        return jsonify({"message": "Item deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete item"}), 500

@item_routes.route('/items', methods=['GET'])
def get_all_items():
    items_from_db = ItemCRUD.get_all_items()
    items = []
    for item in items_from_db:
        item = {
            "id": item[0],
            "name": item[1],
            "description": item[2],
            "category_id": item[3],
            "selling_price": item[4],
            "quantity": item[5]
        }
        items.append(item)
    if items_from_db and items:
        return jsonify(items), 200
    else:
        return jsonify({"error": "No items found"}), 404
