'''Managing Job Scheduling in a Computing Center 
You are managing a computing center that processes jobs submitted by various departments of an
organization. Jobs are categorized into two priority levels: high priority (system jobs) and low priority (user
jobs). Each job has a specific processing time required for completion.
Here are the details of the jobs currently in the system:
High Priority (System) Jobs:
Job A: Performs critical database backups, takes 8 units of time to complete.
Job B: Handles real-time monitoring tasks, takes 5 units of time to complete.
Job C: Executes system updates, takes 10 units of time to complete.
Low Priority (User) Jobs:
Job D: Runs periodic report generation, takes 6 units of time to complete.
Job E: Processes email delivery, takes 3 units of time to complete.
Job F: Executes batch data processing, takes 7 units of time to complete.
Implement the Multi-Level Queue Scheduling algorithm where high priority (system) jobs are scheduled
with higher priority compared to low priority (user) jobs. Within each queue (high and low priority), jobs are
scheduled using FCFS.
Your task is to simulate the scheduling of these jobs and calculate the total time required to complete all
jobs, considering the priorities and FCFS scheduling within each queue.
Input: Processing times for each job in the high and low priority queues.
High Priority Jobs:
Job A: 8 units
Job B: 5 units
Job C: 10 units
Low Priority Jobs:
Job D: 6 units
Job E: 3 units
Job F: 7 units
Output: The total time (in units) required to complete all jobs.
39 units
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

high_priority_jobs = {'Job A': 8, 'Job B': 5, 'Job C': 10,}
low_priority_jobs = {'Job D': 6, 'Job E': 3, 'Job F': 7,}
total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
