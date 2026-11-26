from app.my_project.auth.domain.address import Address
from app.my_project.auth.domain.watch import Watch
from app import db 

class AddressDAO:
    def find_all(self):
        return Address.query.all()

    def find_by_id(self, address_id):
        return Address.query.get(address_id)

    def create(self, address: Address):
        db.session.add(address)
        db.session.commit()
        return address

    def update(self, address_id: int, data: dict):
        address = self.find_by_id(address_id)
        if address:
            address.city = data.get('city', address.city)
            address.street = data.get('street', address.street)
            address.building = data.get('building', address.building)
            db.session.commit()
        return address

    def delete(self, address_id: int):
        address = self.find_by_id(address_id)
        if address:
            db.session.delete(address)
            db.session.commit()

    # Метод для виводу даних M:1 (годинники за адресою)
    def find_watches_by_address(self, address_id: int):
        return Watch.query.filter(Watch.home_address_id == address_id).all()