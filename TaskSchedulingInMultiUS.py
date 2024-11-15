'''Task Scheduling in a Multi-User System
You are managing a multi-user system where tasks from different users need to be scheduled for
processing. Tasks are categorized into two priority levels: high priority (system tasks) and low priority (user
tasks). Each task has a specific processing time required for completion.
Here are the details of the tasks currently in the system:
High Priority (System) Tasks:
Task A: Performs critical system maintenance, takes 12 units of time to complete.
Task B: Executes essential security updates, takes 8 units of time to complete.
Task C: Handles real-time data processing, takes 15 units of time to complete.
Low Priority (User) Tasks:
Task D: Runs a background data synchronization process, takes 6 units of time to complete.
Task E: Processes user-generated reports, takes 4 units of time to complete.
Task F: Executes regular data backups, takes 10 units of time to complete.
Implement the Multi-Level Queue Scheduling algorithm where high priority (system) tasks are scheduled
with higher priority compared to low priority (user) tasks. Within each queue (high and low priority), tasks
are scheduled using FCFS.
Your task is to simulate the scheduling of these tasks and calculate the total time required to complete all
tasks, considering the priorities and FCFS scheduling within each queue.
Input: Processing times for each task in the high and low priority queues.
High Priority Tasks:
Task A: 12 units
Task B: 8 units
Task C: 15 units
Low Priority Tasks:
Task D: 6 units
Task E: 4 units
Task F: 10 units
Output: The total time (in units) required to complete all tasks.
55 units
'''

from queue import Queue
def calculate_total_time(high_priority_tasks, low_priority_tasks):
    priortask_queue=Queue()
    for task, time in high_priority_tasks.items():
        priortask_queue.put((task, time))
    for task, time in low_priority_tasks.items():
        priortask_queue.put((task, time))
    total_time=0
    while not priortask_queue.empty():
        task, time=priortask_queue.get()
        total_time+=time
    return total_time
    
          
high_priority_tasks = {'Task A': 12, 'Task B': 8, 'Task C': 15,}
low_priority_tasks = {'Task D': 6, 'Task E': 4, 'Task F': 10, }
total_time = calculate_total_time(high_priority_tasks, low_priority_tasks)
print(f"The total time required to complete all tasks is: {total_time} units")
