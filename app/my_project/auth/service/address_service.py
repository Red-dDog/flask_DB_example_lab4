from app.my_project.auth.dao.address_dao import AddressDAO
from app.my_project.auth.domain.address import Address

class AddressService:
    def __init__(self):
        self.address_dao = AddressDAO()

    def get_all_addresses(self):
        addresses = self.address_dao.find_all()
        return [address.put_into_dto() for address in addresses]

    def get_address_by_id(self, address_id):
        address = self.address_dao.find_by_id(address_id)
        return address.put_into_dto() if address else None

    def create_address(self, data):
        new_address = Address(
            city=data.get('city'),
            street=data.get('street'),
            building=data.get('building')
        )
        created_address = self.address_dao.create(new_address)
        return created_address.put_into_dto()

    def update_address(self, address_id, data):
        updated = self.address_dao.update(address_id, data)
        return updated.put_into_dto() if updated else None

    def delete_address(self, address_id):
        self.address_dao.delete(address_id)

    # Логіка для M:1
    def get_watches_by_address(self, address_id):
        watches = self.address_dao.find_watches_by_address(address_id)
        return [watch.put_into_dto() for watch in watches]