from flask import jsonify
from app.my_project.auth.service.watch_model_service import WatchModelService

watch_model_service = WatchModelService()

class WatchModelController:
    # Контролер для M:M
    @staticmethod
    def get_features_by_model(model_id):
        features = watch_model_service.get_features_by_model(model_id)
        return jsonify(features), 200