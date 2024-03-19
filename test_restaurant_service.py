import pytest
from app.api.models import RestaurantIn, RestaurantOut

restaurant = RestaurantIn(
    name='Blackstar',
    address='Moscow',
    menu='beef',
    phone='+7123456789'
)


def test_create_restaurant(restaurant: RestaurantIn = restaurant):
    assert dict(restaurant) == {'name': restaurant.name,
                              'address': restaurant.address,
                              'menu': restaurant.menu,
                              'phone': restaurant.phone
                              }


def test_update_restaurant_menu(restaurant: RestaurantIn = restaurant):
    restaurant_upd = RestaurantOut(
        name='Blackstar',
        address='Moscow',
        menu='beef',
        phone='+7123456789',
        id=1
    )
    assert dict(restaurant_upd) == {'name': restaurant.name,
                              'address': restaurant.address,
                              'menu': restaurant.menu,
                              'phone': restaurant.phone,
                              'id': restaurant_upd.id
                              }


def test_update_restaurant_genre(restaurant: RestaurantIn = restaurant):
    restaurant_upd = RestaurantOut(
        name=restaurant.name,
        address=restaurant.address,
        city=restaurant.city,
        phone = restaurant.phone,
        id=1
    )
    assert dict(restaurant_upd) == {'name': restaurant.name,
                              'address': restaurant.address,
                              'city': restaurant.city,
                              'phone': restaurant.phone,
                              'id': restaurant_upd.id
                              }
