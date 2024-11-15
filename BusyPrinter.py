''' The Busy Printer
Imagine a IARE computer lab with a single printer that serves multiple students. The lab operates on a firstcome, first-served basis for print jobs.
One morning, the lab opens, and the printer is ready to accept jobs. The following print jobs arrive in
sequence:
Job A: Submitted by A, consisting of 10 pages.
Job B: Submitted by B, consisting of 5 pages.
Job C: Submitted by C, consisting of 3 pages.
Job D: Submitted by D, consisting of 7 pages.
Each job arrives at the lab at different times, and they start printing immediately upon arrival. The printer
processes each job in the order it arrives, and each job completes printing without interruption.
Your task is to simulate the FCFS scheduling algorithm for these print jobs and calculate the total time taken
to complete all printing tasks, assuming that the printer prints at a rate of 1 page per second.
Input: The arrival time of each job (in seconds). The number of pages to be printed for each job.
Job A: Arrival time = 0 seconds, Pages = 10
Job B: Arrival time = 1 second, Pages = 5
Job C: Arrival time = 3 seconds, Pages = 3
Job D: Arrival time = 5 seconds, Pages = 7
Output: The total time (in seconds) taken to complete all printing tasks.
27 seconds
'''

def calculate_total_time(arrival_times, pages):
    current_time = 0
    total_time = 0
    for i in range(len(arrival_times)):
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        current_time += pages[i] 
    return current_time
arrival_times = [0, 1, 3, 5]
pages = [10, 5, 3, 7] 
total_time = calculate_total_time(arrival_times, pages)
print(f"The total time taken to complete all printing tasks is: {total_time} seconds")
