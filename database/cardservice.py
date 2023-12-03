from datetime import datetime

from database import get_db
from database.models import UserCard, User, Transfer


# Добавления карты
def add_card_db(user_id, card_number, balance, card_name):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_number=card_number).first()
    if not checker:
        new_card = UserCard(user_id=user_id, card_number=card_number,
                            balance=balance, card_name=card_name,
                            reg_date=datetime.now())
        db.add(new_card)
        db.commit()
        return 'Карта успешно добавлено'
    else:
        return 'Все хуйня, давай по новой'


# Вывести все карты определенного пользователя через user_id
def get_exact_user_cards_db(user_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).first()

    return exact_user_card


# Удаления карту
def delete_card_db(card_id):
    db = next(get_db())
    card = db.query(UserCard).filter_by(card_id=card_id).first()
    if card:
        db.delete(card)
        db.commit()
        return 'Карта удалена'
    else:
        return 'Такой карты не сущ'


def validate_card_db(card_id):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_id).first()
    if checker:
        return checker
    else:
        return False


def get_all_transactions_db(card_id):
    db = next(get_db())
    checker_card = db.query(UserCard).filter_by(card_id=card_id).first()
    if checker_card:
        transfers = db.query(Transfer).filter_by(card_from_id=card_id).all()
        if transfers:
            return transfers
        else:
            return 'Пока нет оплат'
    else:
        return 'Такой карты нет'


def all_cards():
    db = next(get_db())
    cards = db.query(UserCard).all()
    return cards
