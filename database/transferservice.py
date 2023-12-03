from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db

# checekr for card for making transaction
def validate_card(card_number, db):
    db = next(get_db())

    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card

def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    checker_card_from = validate_card((card_from, db))
    checker_card_to = validate_card((card_to, db))

    if checker_card_from and checker_card_to:
        if checker_card_from.balance >= amount:
            checker_card_from.balance -= amount
            checker_card_to.balance +=amount

            # Saving in db
            new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to,
                                       amount=amount, transaction_date=datetime.now())

            db.add(new_transaction)
            db.commit()

            return "transaction was successfully done"
        else:
            return "not enough amount"

    else:
        return "one of the card does not exist"



def get_card_transaction_db(card_from_id):
    db = next(get_db())


    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction

def cancel_transfer_db(card_from, card_to, amount, transfer_id):
    pass
    # db = next(get_db())
    #
    # checker_card_from = validate_card((card_from, db))
    # checker_card_to = validate_card((card_to, db))
    #
    # if checker_card_from and checker_card_to:
    #     if checker_card_from.balance >= amount:
    #         checker_card_from.balance -= amount
    #         checker_card_to.balance += amount
    #
    #         # Saving in db
    #         new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to,
    #                                    amount=amount, transaction_date=datetime.now())
    #
    #         db.add(new_transaction)
    #         db.commit()
    #
    #         return "transaction was successfully done"
    #     else:
    #         return "not enough amount
