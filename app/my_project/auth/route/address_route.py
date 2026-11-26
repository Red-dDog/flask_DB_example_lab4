from flask import Blueprint
from app.my_project.auth.controller.address_controller import AddressController

address_bp = Blueprint('address_bp', __name__, url_prefix='/addresses')

address_bp.route('', methods=['GET'])(AddressController.get_all_addresses)
address_bp.route('/<int:address_id>', methods=['GET'])(AddressController.get_address)
address_bp.route('', methods=['POST'])(AddressController.create_address)
address_bp.route('/<int:address_id>', methods=['PUT'])(AddressController.update_address)
address_bp.route('/<int:address_id>', methods=['DELETE'])(AddressController.delete_address)

# Маршрут для отримання годинників за адресою (зв'язок M:1)
address_bp.route('/<int:address_id>/watches', methods=['GET'])(AddressController.get_watches_by_address)