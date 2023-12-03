from fastapi import FastAPI

from user.user_api import user_router
from card.card_api import card_router

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(card_router)


@app.get('/home')
async def home():
    return {'message': 'hello this is home'}
