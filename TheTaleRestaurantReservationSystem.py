'''The Tale of the Restaurant Reservation System
Imagine a popular restaurant named Gourmet Haven that uses an automated reservation system to manage
table bookings. The restaurant has a limited number of tables, and the reservation system must handle
concurrent booking requests efficiently while ensuring that no table is double-booked.
Gourmet Haven operates with:
• Tables: The restaurant has 10 tables, each with a unique ID.
• Reservation System: A central system that processes reservation requests from multiple
customers.
Reservation System faces the following challenges:
• Concurrency: Multiple customers might attempt to book the same table at the same time.
• Data Integrity: The system must ensure that each table is reserved for only one customer at a time
and that all reservation details are correctly updated.
'''

import threading
import time
import random

class ReservationSystem:
    def __init__(self, num_tables):
        self.tables = {f'Table{i + 1}': True for i in range(num_tables)}  # True means available
        self.lock = threading.Lock()

    def reserve_table(self, table_id):
        with self.lock:
            if self.tables.get(table_id, False):  # Check if the table is available
                print(f"{threading.current_thread().name} reserved {table_id}")
                self.tables[table_id] = False  # Mark the table as reserved
                return True
            else:
                print(f"{threading.current_thread().name} failed to reserve {table_id} (already reserved)")
                return False

    def release_table(self, table_id):
        with self.lock:
            if table_id in self.tables and not self.tables[table_id]:  # Check if the table is reserved
                print(f"{threading.current_thread().name} released {table_id}")
                self.tables[table_id] = True
            else:
                print(f"{threading.current_thread().name} tried to release {table_id}, but it's already available or doesn't exist")

def customer_request(reservation_system, table_id):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate some processing time
    reserved = reservation_system.reserve_table(table_id)
    if reserved:
        time.sleep(random.uniform(0.1, 0.3))
        reservation_system.release_table(table_id)

# Driver Code
reservation_system = ReservationSystem(num_tables=10)
threads = []
table_ids = [f'Table{i + 1}' for i in range(10)]  # List of available tables

for i in range(20):
    table_id = random.choice(table_ids)
    t = threading.Thread(target=customer_request, args=(reservation_system, table_id),
                         name=f"Customer-{i + 1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All reservations completed.")
