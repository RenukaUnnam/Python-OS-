''' Managing Print Jobs in a Shared Printing Environment
You are managing a shared printing environment where print jobs from different departments are queued
up for processing. Print jobs are categorized into two priority levels: high priority (system jobs) and low
priority (user jobs). Each job has a specific processing time required for printing.
Here are the details of the print jobs currently in the system:
High Priority (System) Print Jobs:
Job A: Urgent report for management, takes 15 units of time to print.
Job B: Critical financial statement, takes 10 units of time to print.
Job C: Emergency document for legal department, takes 20 units of time to print.
Low Priority (User) Print Jobs:
Job D: Regular office memo, takes 5 units of time to print.
Job E: Marketing flyer, takes 8 units of time to print.
Job F: Personal document for an employee, takes 3 units of time to print.
Implement the Multi-Level Queue Scheduling algorithm where high priority (system) print jobs are
scheduled with higher priority compared to low priority (user) print jobs. Within each queue (high and low
priority), print jobs are scheduled using FCFS.
Your task is to simulate the scheduling of these print jobs and calculate the total time required to complete
all print jobs, considering the priorities and FCFS scheduling within each queue.
Input: Printing times for each job in the high and low priority queues.
High Priority Print Jobs:
Job A: 15 units
Job B: 10 units
Job C: 20 units
Low Priority Print Jobs:
Job D: 5 units
Job E: 8 units
Job F: 3 units
Output: The total time (in units) required to complete all print jobs.
61 units
'''
from queue import Queue

def calculate_total_time(high_priority_jobs, low_priority_jobs):
    prior_queue = Queue()
    for prior, time in high_priority_jobs.items():
        prior_queue.put((prior, time))
    for process, time in low_priority_jobs.items():
        prior_queue.put((prior, time))
    total_time = 0
    while not prior_queue.empty():
        prior, time = prior_queue.get()
        total_time += time
    return total_time

high_priority_jobs = {'Job A': 15, 'Job B': 10, 'Job C': 20,}
low_priority_jobs = {'Job D': 5, 'Job E': 8, 'Job F': 3,}
total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")



