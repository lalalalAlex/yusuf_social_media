from fastapi import APIRouter
from datetime import datetime

from card import CardAddValidator
from database.cardservice import get_exact_user_cards_db, get_all_transactions_db, all_cards, delete_card_db

card_router = APIRouter(prefix='/card', tags=[' work with cards'])


@card_router.post('/add-card')
async def get_exact_user_card(data: CardAddValidator):
    card = data.model_dump()
    result = add_card_db(**card)
    return {'message': result}


@card_router.get('/all-transfers')
async def transfers_card(card_id: int):
    result = get_all_transactions_db(card_id)
    return {'message': result}


@card_router.get('/get-exact-card')
async def get_exact_card(user_id: int):
    result = get_exact_user_cards_db(user_id)
    return {'message': result}


@card_router.delete('/delete-card')
async def delete_card(card_id: int):
    result = delete_card_db(card_id)
    return {'message': result}


@card_router.get('/all-cards')
async def all_card():
    result = all_cards()
    return {'message': result}
