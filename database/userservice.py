from datetime import datetime
from database.models import User
from database import get_db


def register_db(name, surname, email, password, city, phone_number):
    db = next(get_db())
    checker = check_user_email_db(email)
    if checker:
        return 'Аккаунт уже создан'
    else:
        user = User(name=name, last_name=surname, email=email, password=password, city=city, phone_number=phone_number, reg_date=datetime.now())
        db.add(user)
        db.commit()
        return 'Успешно'


def get_exact_user_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()

    return checker


def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return False


def edit_user_db(user_id, edit_type, new_data):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        if edit_type == 'email':
            checker.email = new_data
        elif edit_type == 'password':
            checker.password = new_data

        db.commit()
        return 'Успешно'
    else:
        return 'Все хуйня, давай по новой'


def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return "user successfully deleted"
    else:
        return "user not found"




