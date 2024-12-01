'''The C-SCAN Disk Scheduling Quest at TechFusion Labs
At TechFusion Labs, a cutting-edge research facility, disk drives are crucial for storing and managing vast
amounts of scientific data. To efficiently handle disk access requests, the facility uses the Circular SCAN (CSCAN) disk scheduling algorithm. This algorithm is chosen for its ability to provide fair access to disk
resources by continuously moving in one direction and wrapping around to handle all pending requests.
The disk drive at TechFusion Labs has 8,000 tracks, numbered from 0 to 7999. The disk head starts at track
3500 and is currently moving towards higher-numbered tracks.
Throughout the day, the following disk access requests are made:
Request A: Track 3800
Request B: Track 600
Request C: Track 7000
Request D: Track 1500
Request E: Track 2500
Simulate the C-SCAN algorithm to determine the order in which the disk head will process the requests.
Calculate the total head movement required to service all the requests using the C-SCAN algorithm, given
that the disk head starts at track 3500 and moves in the direction of higher-numbered tracks.
'''

def cscan_disk_scheduling(initial_head, requests, max_track=7999):
    total_head_movement = 0
    tracks_visited = []

    sorted_requests = sorted(requests)

    upward_requests = [r for r in sorted_requests if r >= initial_head]
    downward_requests = [r for r in sorted_requests if r < initial_head]

    for request in upward_requests:
        total_head_movement += abs(request - initial_head)
        tracks_visited.append(request)
        initial_head = request

    if upward_requests:
        total_head_movement += abs(max_track - initial_head)
        tracks_visited.append(max_track)
        initial_head = max_track

    total_head_movement += abs(max_track - 0)
    tracks_visited.append(0)
    initial_head = 0

    for request in downward_requests:
        total_head_movement += abs(request - initial_head)
        tracks_visited.append(request)
        initial_head = request

    return total_head_movement, tracks_visited


# Driver Code
initial_head_position = 3500
disk_requests = [3800, 600, 7000, 1500, 2500]

total_head_movement, tracks_visited = cscan_disk_scheduling(
    initial_head_position, disk_requests, max_track=7999
)

print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
