'''Job Scheduling in a Computing Cluster
You are managing a computing cluster that processes jobs submitted by various departments of a research
institution. Jobs are categorized into three priority levels: high priority (critical jobs), medium priority
(standard jobs), and low priority (background jobs). Each job has a specific processing time required for
completion.
Here are the details of the jobs currently in the system:
High Priority (Critical) Jobs:
Job A: Performs complex simulations for a time-sensitive research project, takes 20 units of time to
complete.
Job B: Analyzes large datasets for an urgent analysis, takes 15 units of time to complete.
Job C: Executes critical experiments with strict deadlines, takes 25 units of time to complete.
Medium Priority (Standard) Jobs:
Job D: Runs routine data processing tasks, takes 10 units of time to complete.
Job E: Processes experimental results for ongoing studies, takes 12 units of time to complete.
Job F: Executes regular system maintenance tasks, takes 8 units of time to complete.
Low Priority (Background) Jobs:
Job G: Performs non-critical data backups, takes 5 units of time to complete.
Job H: Runs periodic log file analysis, takes 4 units of time to complete.
Job I: Executes routine software updates, takes 6 units of time to complete.
Implement the Multi-Level Queue Scheduling algorithm where jobs are scheduled based on their priority
levels: high priority jobs are scheduled first, followed by medium priority jobs, and then low priority jobs.
Within each priority level, jobs are scheduled using FCFS.
Your task is to simulate the scheduling of these jobs and calculate the total time required to complete all
jobs, considering the priorities and FCFS scheduling within each priority level.
Input: Processing times for each job in the high, medium, and low priority queues.
High Priority Jobs:
Job A: 20 units
Job B: 15 units
Job C: 25 units
Medium Priority Jobs:
Job D: 10 units
Job E: 12 units
Job F: 8 units
Low Priority Jobs:
Job G: 5 units
Job H: 4 units
Job I: 6 units
Output: The total time (in units) required to complete all jobs.
105 units
'''

from queue import Queue
def calculate_total_time(high_priority_jobs, medium_priority_jobs, low_priority_jobs):
    prior_queue = Queue()
    for prior, time in high_priority_jobs.items():
        prior_queue.put((prior, time))
    for process, time in medium_priority_jobs.items():
        prior_queue.put((prior, time))
    for process, time in low_priority_jobs.items():
        prior_queue.put((prior, time))
    total_time = 0
    while not prior_queue.empty():
        prior, time = prior_queue.get()
        total_time += time
    return total_time # Driver Code
high_priority_jobs = {'Job A': 20, 'Job B': 15, 'Job C': 25,}
medium_priority_jobs = {'Job D': 10, 'Job E': 12, 'Job F': 8,}
low_priority_jobs = {'Job G': 5, 'Job H': 4, 'Job I': 6,}
total_time = calculate_total_time(high_priority_jobs, medium_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
