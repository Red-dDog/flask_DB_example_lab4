from flask import request, jsonify
from app.my_project.auth.service.address_service import AddressService

address_service = AddressService()

class AddressController:
    @staticmethod
    def get_all_addresses():
        return jsonify(address_service.get_all_addresses()), 200

    @staticmethod
    def get_address(address_id):
        address = address_service.get_address_by_id(address_id)
        if address:
            return jsonify(address), 200
        return jsonify({"message": "Address not found"}), 404

    @staticmethod
    def create_address():
        data = request.get_json()
        new_address = address_service.create_address(data)
        return jsonify(new_address), 201

    @staticmethod
    def update_address(address_id):
        data = request.get_json()
        updated = address_service.update_address(address_id, data)
        if updated:
            return jsonify(updated), 200
        return jsonify({"message": "Address not found"}), 404

    @staticmethod
    def delete_address(address_id):
        address_service.delete_address(address_id)
        return jsonify({"message": "Address deleted"}), 204

    # Контролер для M:1
    @staticmethod
    def get_watches_by_address(address_id):
        watches = address_service.get_watches_by_address(address_id)
        return jsonify(watches), 200