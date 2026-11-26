from app.my_project.auth.domain.user import User
from app import db 

class UserDAO:
    def find_all(self):
        return User.query.all()

    def find_by_id(self, user_id):
        return User.query.get(user_id)

    def create(self, user: User):
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user_id: int, data: dict):
        user = self.find_by_id(user_id)
        if user:
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.phone = data.get('phone', user.phone)
            user.email = data.get('email', user.email)
            db.session.commit()
        return user

    def delete(self, user_id: int):
        user = self.find_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()