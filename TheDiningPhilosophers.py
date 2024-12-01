'''The Dining Philosophers
In a dining hall, there are 5 philosophers sitting around a round table. Each philosopher needs two utensils
to eat: one in the left hand and one in the right hand. The table has 5 utensils, each placed between two
philosophers.
The philosophers are:
Philosopher 1: Needs utensils U1 and U2.
Philosopher 2: Needs utensils U2 and U3.
Philosopher 3: Needs utensils U3 and U4.
Philosopher 4: Needs utensils U4 and U5.
Philosopher 5: Needs utensils U5 and U1.
Each philosopher picks up the utensil on their left and then tries to pick up the utensil on their right. If they
cannot pick up both utensils, they put down the one they have and wait.
Analyze the system for potential deadlock. What strategies can be used to prevent or resolve the deadlock?
'''

import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, philosopher_id, left_utensil, right_utensil):
        super().__init__()
        self.philosopher_id = philosopher_id  # Unique ID for the philosopher
        self.left_utensil = left_utensil      # Left utensil (Lock)
        self.right_utensil = right_utensil    # Right utensil (Lock)

    def run(self):
        while True:  # Continuous cycle of thinking and eating
            self.think()
            self.eat()

    def think(self):
        print(f"Philosopher {self.philosopher_id} is thinking.")
        time.sleep(random.uniform(1, 3))  # Simulate thinking for a random time

    def eat(self):
        left_first = self.philosopher_id % 2 == 0 
        first_utensil = self.left_utensil if left_first else self.right_utensil
        second_utensil = self.right_utensil if left_first else self.left_utensil

        with first_utensil:
            with second_utensil:
                print(f"Philosopher {self.philosopher_id} is eating.")
                time.sleep(random.uniform(1, 2))  # Simulate eating for a random time
                print(f"Philosopher {self.philosopher_id} finished eating.")

# Driver Code
num_philosophers = 5
utensils = [threading.Lock() for _ in range(num_philosophers)]
philosophers = []

# Create Philosopher threads
for i in range(num_philosophers):
    left_utensil = utensils[i]
    right_utensil = utensils[(i + 1) % num_philosophers]
    philosopher = Philosopher(i + 1, left_utensil, right_utensil)
    philosophers.append(philosopher)

# Start all Philosopher threads
for philosopher in philosophers:
    philosopher.start()

# Allow simulation to run indefinitely
for philosopher in philosophers:
    philosopher.join()
