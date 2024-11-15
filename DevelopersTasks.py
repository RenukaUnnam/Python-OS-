'''The Software Developer's Tasks
Sophia, a software developer, has several programming tasks to complete in her project. Each task requires
a different amount of time to finish. She decides to use the SJF scheduling algorithm to manage her tasks
efficiently.
Here are the tasks she needs to complete:
• Task A: Writing a simple utility function, which takes 3 hours.
• Task B: Debugging a critical issue in the main application, which takes 5 hours.
• Task C: Refactoring a complex module, which takes 7 hours.
• Task D: Testing and documenting a new feature, which takes 4 hours.
Sophia decides to implement the SJF algorithm for scheduling these tasks based on their execution times.
Your task is to simulate the SJF scheduling algorithm for Sophia's tasks and calculate the total time required
to complete all tasks, assuming that each task starts immediately after the previous one is completed.
Input: Execution times of each task.
Task A: 3 hours
Task B: 5 hours
Task C: 7 hours
Task D: 4 hours
Output: The total time (in hours) required to complete all tasks.
19 hours
'''

def calculate_total_time(execution_times):
 total_time = sum(execution_times)
 return total_time
execution_times = [3, 5, 7, 4] 
total_time = calculate_total_time(execution_times)
print(f"The total time required to complete all tasks is: {total_time} hours") 
