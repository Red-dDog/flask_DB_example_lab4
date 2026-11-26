from app.my_project.auth.domain.watch_model import WatchModel

class WatchModelDAO:
    def find_by_id(self, model_id):
        return WatchModel.query.get(model_id)

    # Метод для зв'язку M:M
    def find_features_by_model(self, model_id):
        model = self.find_by_id(model_id)
        if model:
            return model.features
        return []