from flask import Blueprint
from app.my_project.auth.controller.watch_model_controller import WatchModelController

watch_model_bp = Blueprint('watch_model_bp', __name__, url_prefix='/watch_models')

# Маршрут для отримання функцій за моделлю годинника (зв'язок M:M)
watch_model_bp.route('/<int:model_id>/features', methods=['GET'])(WatchModelController.get_features_by_model)