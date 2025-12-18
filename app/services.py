from app.models import User
from app import db


class UserService:
    @staticmethod
    def create_user(username, email):
        if db.session.query(User).filter_by(username=username).first():
            raise ValueError('Username already exists')

        if db.session.query(User).filter_by(email=email).first():
            raise ValueError('Email already exists')

        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def get_all_users():
        return db.session.query(User).all()

    @staticmethod
    def delete_user(user_id):
        user = db.session.get(User, user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False