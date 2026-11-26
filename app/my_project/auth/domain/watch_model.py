from app import db

class WatchModel(db.Model):
    __tablename__ = 'watch_models'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(50), nullable=False)
    model_name = db.Column(db.String(100), nullable=False)

    # Зв'язок M:M з таблицею features через watch_model_features
    features = db.relationship('Feature', secondary='watch_model_features', backref='watch_models')

    def put_into_dto(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model_name": self.model_name
        }