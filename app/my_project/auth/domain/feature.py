from app import db

class Feature(db.Model):
    __tablename__ = 'features'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feature_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    def put_into_dto(self):
        return {
            "id": self.id,
            "feature_name": self.feature_name,
            "description": self.description
        }