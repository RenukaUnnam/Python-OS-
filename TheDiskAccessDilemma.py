''' The Disk Access Dilemma
In a busy computer lab at Techville University, a large disk drive serves the needs of multiple students. The
disk drive handles requests from several applications running on different computers. Each request involves
accessing a specific track on the disk. The disk drive operates under the First-Come, First-Served (FCFS)
scheduling algorithm, meaning that requests are handled in the order they are received, regardless of their
location on the disk.
Imagine the disk drive has 1000 tracks, numbered 0 through 999. The disk's current head position is at track
150. Over the course of a few minutes, the following disk access requests are made by different applications:
Request 1: Track 200
Request 2: Track 50
Request 3: Track 800
Request 4: Track 300
Request 5: Track 100
The requests are received in the order listed above.
Problem:
1. Calculate the total head movement required to satisfy all the requests using the FCFS algorithm.
2. Determine the order of tracks that the disk head will visit, starting from the initial position.
'''

def fcfs_disk_scheduling(initial_head, requests):
    total_head_movement = 0
    tracks_visited = [initial_head] 
    
    current_position = initial_head
    
    for request in requests:
        movement = abs(request - current_position)
        total_head_movement += movement
        
        current_position = request
        
        tracks_visited.append(current_position)
    
    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 150
disk_requests = [200, 50, 800, 300, 100]

total_head_movement, tracks_visited = fcfs_disk_scheduling(initial_head_position, disk_requests)

print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
