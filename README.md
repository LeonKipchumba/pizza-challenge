# 🍕 Pizza Challenge

A Flask MVC API for managing restaurants, pizzas, and their relationships.

---

## 🧰 Setup

```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
```

---

## 🗂 Structure

- `server/models/` — SQLAlchemy models
- `server/controllers/` — Route logic
- `server/app.py` — App setup
- `server/seed.py` — Seed script

---

## 🛠 Models

- **Restaurant**: id, name, address, has many RestaurantPizzas (cascade delete)
- **Pizza**: id, name, ingredients, has many RestaurantPizzas
- **RestaurantPizza**: id, price (1-30), restaurant_id, pizza_id

---

## 🎯 Routes

| Method | Endpoint                  | Description                                 |
|--------|---------------------------|---------------------------------------------|
| GET    | /restaurants              | List all restaurants                        |
| GET    | /restaurants/<id>         | Restaurant details + pizzas                 |
| DELETE | /restaurants/<id>         | Delete restaurant & related RestaurantPizzas|
| GET    | /pizzas                   | List all pizzas                             |
| POST   | /restaurant_pizzas        | Create new RestaurantPizza                  |

---

## 📝 Examples

**GET /restaurants**
```json
[{"id":1,"name":"Pizza Place","address":"123 Main St"}]
```

**GET /restaurants/1**
```json
{"id":1,"name":"Pizza Place","address":"123 Main St","pizzas":[{"id":1,"name":"Margherita","ingredients":"Dough, Tomato Sauce, Cheese"}]}
```

**POST /restaurant_pizzas**
Request:
```json
{"price":5,"pizza_id":1,"restaurant_id":3}
```
Success:
```json
{"id":4,"price":5,"pizza_id":1,"restaurant_id":3,"pizza":{"id":1,"name":"Emma","ingredients":"Dough, Tomato Sauce, Cheese"},"restaurant":{"id":3,"name":"Kiki's Pizza","address":"address3"}}
```
Error:
```json
{"errors":["Price must be between 1 and 30"]}
```

---

## ✅ Validation
- `RestaurantPizza.price` must be 1-30
- Deleting a Restaurant also deletes its RestaurantPizzas

---

## 📬 Postman
- Import `challenge-1-pizzas.postman_collection.json` into Postman to test endpoints.
