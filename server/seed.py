from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

# Clear old data and create tables fresh
with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()
    print("Creating new tables...")
    db.create_all()

    # Sample restaurants
    r1 = Restaurant(name="Mama Mia", address="123 Main St")
    r2 = Restaurant(name="Pizza Palace", address="456 Elm St")
    r3 = Restaurant(name="Cheesy Bites", address="789 Oak St")

    # Sample pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Chicken, Onion, Cheese")
    p4 = Pizza(name="Veggie Delight", ingredients="Tomato, Bell Peppers, Olives, Onions, Cheese")

    db.session.add_all([r1, r2, r3, p1, p2, p3, p4])
    db.session.commit()

    # Link restaurants with pizzas through RestaurantPizza
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=15, restaurant=r2, pizza=p3)
    rp4 = RestaurantPizza(price=9, restaurant=r3, pizza=p4)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("✅ Database seeded successfully!")