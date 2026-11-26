from flask import Blueprint
from app.my_project.auth.controller.user_controller import UserController

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

user_bp.route('', methods=['GET'])(UserController.get_all_users)
user_bp.route('/<int:user_id>', methods=['GET'])(UserController.get_user)
user_bp.route('', methods=['POST'])(UserController.create_user)
user_bp.route('/<int:user_id>', methods=['PUT'])(UserController.update_user)
user_bp.route('/<int:user_id>', methods=['DELETE'])(UserController.delete_user)