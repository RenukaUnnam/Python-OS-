'''Emergency Room Prioritization
You are managing an emergency room in a hospital where patients arrive with different medical conditions.
Each patient requires a different level of urgency for treatment. To ensure critical cases are handled
promptly, you decide to implement the Priority Scheduling algorithm for patient treatment.
Here are the details of the patients currently in the emergency room:
Patient A: Has suffered a heart attack and requires immediate attention, priority level 1.
Patient B: Has a broken arm and needs urgent treatment, priority level 2.
Patient C: Has a high fever and needs attention soon, priority level 3.
Patient D: Has a minor cut and can wait, priority level 4.
You decide to implement Priority Scheduling where patients with higher priority levels are treated first. If
two patients have the same priority level, they are treated in the order they arrived.
Your task is to simulate the Priority Scheduling algorithm for treating these patients and calculate the total
time required to treat all patients, considering their priority levels.
Input: Priority levels of each patient. Treatment times for each patient.
Patient A: Priority 1, Treatment time 10 minutes
Patient B: Priority 2, Treatment time 8 minutes
Patient C: Priority 3, Treatment time 15 minutes
Patient D: Priority 4, Treatment time 5 minutes
Output: The total time (in minutes) required to treat all patients.
38 minutes
'''

from queue import PriorityQueue
def calculate_total_time(patients):
    pq = PriorityQueue()
    for priority, treatment_time in patients:
        pq.put((priority, treatment_time))
    total_time = 0
    while not pq.empty(): 
        _, treatment_time = pq.get()
        total_time += treatment_time 
    return total_time
patients = [
    (1, 10),  # Patient A: Priority 1, Treatment time 10 minutes
    (2, 8),   # Patient B: Priority 2, Treatment time 8 minutes
    (3, 15),  # Patient C: Priority 3, Treatment time 15 minutes
    (4, 5)    # Patient D: Priority 4, Treatment time 5 minutes
]
total_time = calculate_total_time(patients)
print(f"The total time required to treat all patients is: {total_time} minutes")
