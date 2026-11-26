from app import db

class WatchModelFeature(db.Model):
    __tablename__ = 'watch_model_features'
    
    model_id = db.Column(db.Integer, db.ForeignKey('watch_models.id'), primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey('features.id'), primary_key=True)