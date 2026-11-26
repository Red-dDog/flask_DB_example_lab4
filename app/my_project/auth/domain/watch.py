from app import db

class Watch(db.Model):
    __tablename__ = 'watches'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    model_id = db.Column(db.Integer, nullable=True) # Поки без зв'язку для спрощення
    
    # Зв'язки з іншими таблицями
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    wearer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    home_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=True)

    # Relationships для зручного витягування даних
    owner = db.relationship('User', foreign_keys=[owner_id])
    wearer = db.relationship('User', foreign_keys=[wearer_id])
    home_address = db.relationship('Address', foreign_keys=[home_address_id])

    def put_into_dto(self):
        return {
            "id": self.id,
            "serial_number": self.serial_number,
            "model_id": self.model_id,
            "owner_id": self.owner_id,
            "wearer_id": self.wearer_id,
            "home_address_id": self.home_address_id
        }