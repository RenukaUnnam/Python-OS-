''' The Tale of the Online Shopping Cart System
Imagine a popular online shopping platform called ShopEase. The platform has a feature that allows
customers to add items to their shopping cart and proceed to checkout. Due to high traffic, the system
needs to handle multiple customers accessing and modifying their shopping carts concurrently.
The Problem: ShopEase must ensure:
• Concurrency: Multiple customers may attempt to add or remove the same item from their cart
simultaneously.
• Data Integrity: The system must maintain accurate item counts and prevent inconsistencies in the
shopping cart data.
ShopEase operates with:
• Shopping Carts: Each customer has a unique shopping cart that can be modified.
• Inventory System: The inventory tracks the availability of items and is updated when items are
added or removed from carts.
'''

import threading
import time
import random

class InventorySystem:
    def __init__(self):
        self.inventory = {'Item1': 50, 'Item2': 30, 'Item3': 20}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        with self.lock:
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"Added {quantity} of {item} to inventory. New quantity: {self.inventory[item]}")

    def remove_item(self, item, quantity):
        with self.lock:
            if self.inventory.get(item, 0) >= quantity:
                self.inventory[item] -= quantity
                print(f"Removed {quantity} of {item} from inventory. Remaining: {self.inventory[item]}")
                return True
            else:
                print(f"Failed to remove {quantity} of {item}: Insufficient stock.")
                return False


class ShoppingCart:
    def __init__(self):
        self.carts = {}
        self.lock = threading.Lock()

    def add_to_cart(self, user_id, item, quantity, inventory):
        with self.lock:
            if inventory.remove_item(item, quantity):
                if user_id not in self.carts:
                    self.carts[user_id] = {}
                if item in self.carts[user_id]:
                    self.carts[user_id][item] += quantity
                else:
                    self.carts[user_id][item] = quantity
                print(f"{user_id} added {quantity} of {item} to cart.")
                return True
            else:
                print(f"{user_id} failed to add {quantity} of {item} to cart (insufficient stock).")
                return False

    def remove_from_cart(self, user_id, item, quantity, inventory):
        with self.lock:
            if user_id in self.carts and self.carts[user_id].get(item, 0) >= quantity:
                self.carts[user_id][item] -= quantity
                if self.carts[user_id][item] == 0:
                    del self.carts[user_id][item]
                inventory.add_item(item, quantity)
                print(f"{user_id} removed {quantity} of {item} from cart.")
                return True
            else:
                print(f"{user_id} failed to remove {quantity} of {item} from cart (not enough in cart).")
                return False


def customer_action(user_id, cart, inventory):
    items = list(inventory.inventory.keys())
    action = random.choice(['add', 'remove'])
    item = random.choice(items)
    quantity = random.randint(1, 5)
    if action == 'add':
        cart.add_to_cart(user_id, item, quantity, inventory)
    elif action == 'remove':
        cart.remove_from_cart(user_id, item, quantity, inventory)


# Driver Code
inventory = InventorySystem()
cart = ShoppingCart()
threads = []
user_ids = [f'User{i+1}' for i in range(10)]

for user_id in user_ids:
    for _ in range(5):  # Each user performs 5 actions
        t = threading.Thread(target=customer_action, args=(user_id, cart, inventory))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print("All customer actions completed.")
