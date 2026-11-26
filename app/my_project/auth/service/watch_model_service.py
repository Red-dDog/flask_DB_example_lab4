from app.my_project.auth.dao.watch_model_dao import WatchModelDAO

class WatchModelService:
    def __init__(self):
        self.watch_model_dao = WatchModelDAO()

    # Бізнес-логіка для M:M
    def get_features_by_model(self, model_id):
        features = self.watch_model_dao.find_features_by_model(model_id)
        return [feature.put_into_dto() for feature in features]