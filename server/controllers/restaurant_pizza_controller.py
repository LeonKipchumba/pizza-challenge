from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    errors = []
    if not (isinstance(price, int) and 1 <= price <= 30):
        errors.append("Price must be between 1 and 30")
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if not pizza or not restaurant:
        errors.append("Invalid pizza_id or restaurant_id")
    if errors:
        return jsonify({"errors": errors}), 400
    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()
    return jsonify({
        **rp.to_dict(),
        "pizza": pizza.to_dict(),
        "restaurant": restaurant.to_dict()
    }), 201
