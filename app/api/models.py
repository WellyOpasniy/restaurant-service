from pydantic import BaseModel
from typing import List, Optional

class RestaurantIn(BaseModel):
    name: str
    address: str
    menu: str
    phone: str


class RestaurantOut(RestaurantIn):
    id: int
