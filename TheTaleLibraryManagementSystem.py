'''The Tale of the Library Management System
Imagine a large university library called UniLib, which has an automated system to manage its book
inventory and handle user requests. The system must ensure that book information is consistently updated
and accessible to all users, even when multiple requests are being processed simultaneously.
• Book Checkouts: When a user checks out a book, the system must update the book's availability
status.
• Book Returns: When a user returns a book, the system must update the book's status to available.
• The library has the following setup:
• Book Inventory: A central inventory database that tracks the availability of each book.
• User Requests: Users can check out or return books at any time, and multiple requests can be
processed concurrently.
'''

import threading
import time
import random

class BookInventory:
    def __init__(self):
        self.inventory = {'Book1': True, 'Book2': True, 'Book3': True}
        self.lock = threading.Lock()

    def checkout_book(self, book):
        with self.lock:
            if self.inventory.get(book, False):
                print(f"{threading.current_thread().name} checked out {book}")
                self.inventory[book] = False
            else:
                print(f"{threading.current_thread().name} tried to check out {book}, but it's already checked out")

    def return_book(self, book):
        with self.lock:
            if book in self.inventory and not self.inventory[book]:
                print(f"{threading.current_thread().name} returned {book}")
                self.inventory[book] = True
            else:
                print(f"{threading.current_thread().name} tried to return {book}, but it's not checked out or doesn't exist")

def user_request(inventory, book, action):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate some processing time
    if action == 'checkout':
        inventory.checkout_book(book)
    elif action == 'return':
        inventory.return_book(book)

inventory = BookInventory()
threads = []
books = ['Book1', 'Book2', 'Book3']
actions = ['checkout', 'return']

for i in range(10):
    book = random.choice(books)
    action = random.choice(actions)
    t = threading.Thread(target=user_request, args=(inventory, book, action), name=f"User-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All operations completed.")
