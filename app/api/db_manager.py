from app.api.models import RestaurantIn, RestaurantOut
from app.api.db import restaurants, database


async def add_restaurant(payload: RestaurantIn):
    query = restaurants.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_restaurant():
    query = restaurants.select()
    return await database.fetch_all(query=query)


async def get_restaurant(id):
    query = restaurants.select().where(restaurants.c.id == id)
    return await database.fetch_one(query=query)


async def delete_restaurant(id: int):
    query = restaurants.delete().where(restaurants.c.id == id)
    return await database.execute(query=query)

