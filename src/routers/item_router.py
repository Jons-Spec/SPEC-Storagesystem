from flask import Flask, request, jsonify
from ..components.item_crud import ItemCRUD

class ItemRouter:
    def __init__(self, app: Flask):
        self.app = app

        @app.route('/items', methods=['POST'])
        def create_item():
            data = request.json
            success = ItemCRUD.create_item(**data)
            if success:
                return jsonify({"message": "Item created successfully"}), 201
            else:
                return jsonify({"error": "Failed to create item"}), 500

        @app.route('/items/<int:item_id>', methods=['GET'])
        def get_item(item_id: int):
            item = ItemCRUD.read_item(item_id)
            if item:
                return jsonify(item), 200
            else:
                return jsonify({"error": "Item not found"}), 404

        @app.route('/items/<int:item_id>', methods=['PUT'])
        def update_item(item_id: int):
            data = request.json
            success = ItemCRUD.update_item(item_id, **data)
            if success:
                return jsonify({"message": "Item updated successfully"}), 200
            else:
                return jsonify({"error": "Failed to update item"}), 500

        @app.route('/items/<int:item_id>', methods=['DELETE'])
        def delete_item(item_id: int):
            success = ItemCRUD.delete_item(item_id)
            if success:
                return jsonify({"message": "Item deleted successfully"}), 200
            else:
                return jsonify({"error": "Failed to delete item"}), 500
