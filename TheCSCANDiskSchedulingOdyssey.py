'''The C-SCAN Disk Scheduling Odyssey
In the Advanced Data Center at StellarTech Enterprises, a state-of-the-art disk drive is used to handle highpriority data access requests from various applications. The disk drive uses the Circular SCAN (C-SCAN) disk
scheduling algorithm to manage these requests. C-SCAN is designed to provide a more uniform wait time
by only servicing requests in one direction and then quickly returning to the beginning of the disk to
continue servicing. The disk in the StellarTech data center has 10,000 tracks, numbered from 0 to 9999. The
disk head starts at track 4000 and is currently moving in the direction of higher-numbered tracks.
Over the day, the following disk access requests are made:
Request 1: Track 4200
Request 2: Track 1000
Request 3: Track 6000
Request 4: Track 7500
Request 5: Track 2000
Simulate the C-SCAN algorithm to determine the order in which the disk head will process the requests.
Calculate the total head movement required to service all the requests using the C-SCAN algorithm.
'''

def cscan_disk_scheduling(initial_head, requests, max_track=9999):
    total_head_movement = 0
    tracks_visited = []
    
    sorted_requests = sorted(requests)
    
    upward_requests = [r for r in sorted_requests if r >= initial_head]
    downward_requests = [r for r in sorted_requests if r < initial_head]
    
    for request in upward_requests:
        total_head_movement += abs(request - initial_head)
        initial_head = request
        tracks_visited.append(request)
    
    if upward_requests:
        total_head_movement += abs(max_track - initial_head)
        initial_head = max_track
        tracks_visited.append(max_track)
    
    total_head_movement += abs(max_track - 0)
    initial_head = 0
    tracks_visited.append(0)
    
    for request in downward_requests:
        total_head_movement += abs(request - initial_head)
        initial_head = request
        tracks_visited.append(request)
    
    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 4000
disk_requests = [4200, 1000, 6000, 7500, 2000]

total_head_movement, tracks_visited = cscan_disk_scheduling(
    initial_head_position, disk_requests
)

print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
