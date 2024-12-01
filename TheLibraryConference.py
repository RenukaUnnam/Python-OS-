'''The Library Conference
Imagine a conference being held at a university library, where several research teams are working on their
projects. The library has a set of resources:
3 computers (R1, R2, R3)
2 projectors (P1, P2)
Each team needs access to both a computer and a projector to complete their work. The teams are as
follows:
Team A: Needs 1 computer and 1 projector.
Team B: Needs 1 computer and 1 projector.
Team C: Needs 1 computer and 1 projector.
At any given time, each team is holding a resource while waiting for another resource to complete their
work. The following events occur:
Team A is using computer R1 and waiting for projector P1.
Team B is using projector P2 and waiting for computer R2.
Team C is using computer R3 and waiting for projector P2.
Page | 56
Determine if there is a deadlock in the system. If so, describe the circular wait condition and suggest a way
to prevent or resolve the deadlock.
'''

import threading
import time

resources = {'computers': ['R1', 'R2', 'R3'], 'projectors': ['P1', 'P2']}
team_requests = {
    'TeamA': {'computer': 'R1', 'projector': 'P1'},
    'TeamB': {'computer': 'R2', 'projector': 'P2'},
    'TeamC': {'computer': 'R3', 'projector': 'P2'}
}
allocated_resources = {
    'TeamA': {'computer': None, 'projector': None},
    'TeamB': {'computer': None, 'projector': None},
    'TeamC': {'computer': None, 'projector': None}
}
resource_locks = {
    'computers': {res: threading.Lock() for res in resources['computers']},
    'projectors': {res: threading.Lock() for res in resources['projectors']}
}


def request_resource(team, resource_type, resource):
    """Attempt to acquire a resource lock."""
    lock = resource_locks[resource_type][resource]
    if lock.acquire(timeout=2):  # Wait for 2 seconds to acquire the lock
        allocated_resources[team][resource_type] = resource
        print(f"{team} allocated {resource_type} {resource}")
        return True
    else:
        print(f"{team} failed to allocate {resource_type} {resource}")
        return False


def release_resource(team, resource_type, resource):
    """Release a previously acquired resource lock."""
    lock = resource_locks[resource_type][resource]
    lock.release()
    allocated_resources[team][resource_type] = None
    print(f"{team} released {resource_type} {resource}")


def team_work(team):
    """Simulate a team requesting, using, and releasing resources."""
    print(f"{team} is requesting resources.")
    computer = team_requests[team]['computer']
    projector = team_requests[team]['projector']

    # Try to acquire both resources
    if request_resource(team, 'computers', computer) and request_resource(team, 'projectors', projector):
        print(f"{team} has all resources and is working.")
        time.sleep(2)  # Simulate the team working with resources
        print(f"{team} finished working.")
        release_resource(team, 'computers', computer)
        release_resource(team, 'projectors', projector)
    else:
        # Release any partially acquired resources
        if allocated_resources[team]['computers']:
            release_resource(team, 'computers', computer)
        if allocated_resources[team]['projectors']:
            release_resource(team, 'projectors', projector)


# Create and start threads for each team
threads = []
for team in team_requests.keys():
    thread = threading.Thread(target=team_work, args=(team,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Simulation complete.")
