from app import db

class Address(db.Model):
    __tablename__ = 'addresses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    building = db.Column(db.String(20), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "city": self.city,
            "street": self.street,
            "building": self.building
        }