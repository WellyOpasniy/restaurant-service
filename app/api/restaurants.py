from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import RestaurantOut, RestaurantIn
from app.api import db_manager

restaurants = APIRouter()

@restaurants.post('/', response_model=RestaurantOut, status_code=201)
async def create_restaurant(payload: RestaurantIn):
    restaurant_id = await db_manager.add_restaurant(payload)

    response = {
        'id': restaurant_id,
        **payload.dict()
    }

    return response


@restaurants.get('/', response_model=List[RestaurantOut])
async def get_restaurants():
    return await db_manager.get_all_restaurant()


@restaurants.get('/{id}/', response_model=RestaurantOut)
async def get_restaurant(id: int):
    delivery = await db_manager.get_restaurant(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return delivery


@restaurants.delete('/{id}/', response_model=None)
async def delete_restaurant(id: int):
    delivery = await db_manager.get_restaurant(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return await db_manager.delete_restaurant(id)