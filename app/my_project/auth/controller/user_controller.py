from flask import request, jsonify
from app.my_project.auth.service.user_service import UserService

user_service = UserService()

class UserController:
    @staticmethod
    def get_all_users():
        return jsonify(user_service.get_all_users()), 200

    @staticmethod
    def get_user(user_id):
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({"message": "User not found"}), 404

    @staticmethod
    def create_user():
        data = request.get_json()
        new_user = user_service.create_user(data)
        return jsonify(new_user), 201

    @staticmethod
    def update_user(user_id):
        data = request.get_json()
        updated_user = user_service.update_user(user_id, data)
        if updated_user:
            return jsonify(updated_user), 200
        return jsonify({"message": "User not found"}), 404

    @staticmethod
    def delete_user(user_id):
        user_service.delete_user(user_id)
        return jsonify({"message": "User deleted"}), 204