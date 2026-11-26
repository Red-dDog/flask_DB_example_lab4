from app.my_project.auth.dao.user_dao import UserDAO
from app.my_project.auth.domain.user import User

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def get_all_users(self):
        users = self.user_dao.find_all()
        return [user.put_into_dto() for user in users]

    def get_user_by_id(self, user_id):
        user = self.user_dao.find_by_id(user_id)
        return user.put_into_dto() if user else None

    def create_user(self, data):
        new_user = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone=data.get('phone'),
            email=data.get('email')
        )
        created_user = self.user_dao.create(new_user)
        return created_user.put_into_dto()

    def update_user(self, user_id, data):
        updated_user = self.user_dao.update(user_id, data)
        return updated_user.put_into_dto() if updated_user else None

    def delete_user(self, user_id):
        self.user_dao.delete(user_id)