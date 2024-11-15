'''Managing a Restaurant's Orders
Imagine you are managing a busy restaurant where orders from different tables need to be processed. Each
order requires a different amount of time to be prepared and served. To efficiently manage the kitchen staff
and ensure timely service, you decide to implement the Round Robin scheduling algorithm for processing
orders.
Here are the details of the current orders:
Order from Table 1: Burger and Fries, which takes 5 minutes to prepare.
Order from Table 2: Salad, which takes 3 minutes to prepare.
Order from Table 3: Pizza, which takes 8 minutes to prepare.
Order from Table 4: Pasta, which takes 6 minutes to prepare.
You decide to implement Round Robin with a time quantum of 4 minutes. This means each order will receive
processing time in chunks of 4 minutes until it is completed or until it reaches its final processing time.
Your task is to simulate the Round Robin scheduling algorithm for processing these orders and calculate
the total time required to complete all orders, considering the time quantum.
Input: Processing times of each order. Time quantum for Round Robin scheduling.
Order from Table 1: Burger and Fries (5 minutes)
Order from Table 2: Salad (3 minutes)
Order from Table 3: Pizza (8 minutes)
Order from Table 4: Pasta (6 minutes)
Time Quantum: 4 minutes
Output: The total time (in minutes) required to complete all orders.
22 minutes
'''

from collections import deque
def calculate_total_time(orders, time_quantum):
    order_queue = deque(orders)
    total_time = 0
    while order_queue:
        current_order = order_queue.popleft()
        if current_order <= time_quantum:
            total_time += current_order
        else:
            total_time += time_quantum
            order_queue.append(current_order - time_quantum)
    return total_time
orders = [5, 3, 8, 6]
time_quantum = 4
total_time = calculate_total_time(orders, time_quantum)
print(f"The total time required to complete all orders is: {total_time} minutes")
