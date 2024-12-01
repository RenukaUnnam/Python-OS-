'''The SSTF Disk Scheduling Challenge
The goal of SSTF is to reduce the total seek time by always selecting the request closest to the current head
position. This approach minimizes the movement of the disk head between requests.
Process:
1. Initial State: Start with the initial head position (750 in this case).
2. Select the Closest Request: At each step, identify the request that is closest to the current head
position.
Page | 62
3. Move to the Closest Request: Move the disk head to this closest request and mark it as processed.
4. Update Position and Repeat: Update the current head position to the new track and repeat the
process until all requests are serviced.
'''

def sstf_disk_scheduling(initial_head, requests):
    total_head_movement = 0
    tracks_visited = [initial_head]
    current_position = initial_head
    remaining_requests = requests.copy()  

    while remaining_requests:
        distances = {request: abs(request - current_position) for request in remaining_requests}
        
        closest_request = min(distances, key=distances.get)
        
        movement = distances[closest_request]
        total_head_movement += movement
        current_position = closest_request
        tracks_visited.append(current_position)
        
        remaining_requests.remove(closest_request)

    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 750
disk_requests = [1200, 500, 900, 1500, 300]

total_head_movement, tracks_visited = sstf_disk_scheduling(initial_head_position, disk_requests)

print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
