from server.app import db, app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    # Drop and recreate all tables (for dev only)
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    r1 = Restaurant(name="Pizza Place", address="123 Main St")
    r2 = Restaurant(name="Slice of Heaven", address="456 Elm St")
    r3 = Restaurant(name="Kiki's Pizza", address="address3")
    db.session.add_all([r1, r2, r3])

    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p3 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    db.session.add_all([p1, p2, p3])

    db.session.commit()

    # Seed RestaurantPizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=5, restaurant_id=r3.id, pizza_id=p3.id)
    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded!")
