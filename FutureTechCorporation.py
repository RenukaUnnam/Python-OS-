'''FutureTech Corporation
In the Data Center of FutureTech Corporation, a large disk drive is used to store and retrieve data for various
applications. To manage disk access requests efficiently, the disk drive uses the SCAN disk scheduling
algorithm. This algorithm is often referred to as the "elevator algorithm" because it works similarly to an
elevator in a building: it moves in one direction, servicing requests until it reaches the end, and then reverses
direction to service requests on the way back.
The disk has 5000 tracks, numbered from 0 to 4999. The disk head starts at track 2500 and is currently
moving in the direction of higher-numbered tracks. Over the course of the day, the following disk access
requests are made:
Request 1: Track 2800
Request 2: Track 1500
Request 3: Track 3500
Request 4: Track 4000
Page | 64
Request 5: Track 1000
Problem: Simulate the SCAN algorithm to determine the order in which the disk head will process the
requests. Calculate the total head movement required to service all the requests using the SCAN algorithm,
given that the disk head is initially moving towards higher-numbered tracks.
'''

def scan_disk_scheduling(initial_head, requests, direction='up', max_track=4999):
    total_head_movement = 0
    tracks_visited = []
    
    sorted_requests = sorted(requests)
    
    if direction == 'up':
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
        
        for request in reversed(downward_requests):
            total_head_movement += abs(request - initial_head)
            initial_head = request
            tracks_visited.append(request)
    else:
        downward_requests = [r for r in sorted_requests if r <= initial_head]
        upward_requests = [r for r in sorted_requests if r > initial_head]
        
        for request in reversed(downward_requests):
            total_head_movement += abs(request - initial_head)
            initial_head = request
            tracks_visited.append(request)
        
        if downward_requests:
            total_head_movement += abs(0 - initial_head)
            initial_head = 0
            tracks_visited.append(0)
        
        for request in upward_requests:
            total_head_movement += abs(request - initial_head)
            initial_head = request
            tracks_visited.append(request)

    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 2500
disk_requests = [2800, 1500, 3500, 4000, 1000]

total_head_movement, tracks_visited = scan_disk_scheduling(
    initial_head_position, disk_requests, direction='up'
)

print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
