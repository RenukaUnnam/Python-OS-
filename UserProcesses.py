'''Managing System and User Processes
You are managing a computer system that runs various types of processes, categorized into system
processes and user processes. System processes are critical for the functioning of the operating system and
are given higher priority compared to user processes. To efficiently manage these processes, you decide to
implement a Multi-Level Queue Scheduling algorithm with FCFS scheduling for each queue.
Here's the breakdown of the processes currently in the system:
System Process Queue:
Process A: Handles file system operations, takes 5 units of time to complete.
Process B: Manages memory allocation, takes 3 units of time to complete.
Process C: Performs system updates, takes 7 units of time to complete.
User Process Queue:
Process D: Runs a word processor, takes 4 units of time to complete.
Process E: Executes a media player, takes 2 units of time to complete.
Process F: Performs data analysis, takes 6 units of time to complete.
Implement the Multi-Level Queue Scheduling algorithm where system processes are scheduled with higher
priority compared to user processes. Within each queue (system and user), processes are scheduled using
FCFS.
Your task is to simulate the scheduling of these processes and calculate the total time required to complete
all processes, considering the priorities and FCFS scheduling within each queue.
Input: Processing times for each process in the system and user queues.
System Processes:
Process A: 5 units
Process B: 3 units
Process C: 7 units
User Processes:
Process D: 4 units
Process E: 2 units
Process F: 6 units
Output: The total time (in units) required to complete all processes.
27 units
'''


from queue import Queue

def calculate_total_time(system_processes, user_processes):
    process_queue = Queue()
    for process, time in system_processes.items():
        process_queue.put((process, time))
    for process, time in user_processes.items():
        process_queue.put((process, time))
    total_time = 0
    while not process_queue.empty():
        process, time = process_queue.get()
        total_time += time
    return total_time


system_processes = {'Process A': 5,'Process B': 3,'Process C': 7,}
user_processes = {'Process D': 4, 'Process E': 2, 'Process F': 6,}
total_time = calculate_total_time (system_processes, user_processes)
print(f"The total time required to complete all processes is: {total_time} units")
