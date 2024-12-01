'''Banker's Algorithm
The Banker's algorithm is a deadlock avoidance algorithm used in operating systems to manage resource
allocation and prevent deadlocks. It ensures that resource requests are granted in a way that avoids the
possibility of deadlocks. Let's consider a system with five processes (P1, P2, P3, P4, P5) and three resource
types (R1, R2, R3). The available resources and maximum resource requirements for each process are as
follows:
Page | 59
Available: R1(3), R2(2), R3(2) P1: R1(1), R2(2), R3(2) P2: R1(2), R2(0), R3(1) P3: R1(1), R2(1), R3(1) P4: R1(2),
R2(1), R3(0) P5: R1(0), R2(0), R3(2)
'''

def is_safe_state(processes, available, allocation, need):
    """
    Determines if the system is in a safe state using Banker's Algorithm.
    
    Args:
    processes: List of process names.
    available: List of available resources.
    allocation: 2D list of allocated resources for each process.
    need: 2D list of needed resources for each process.

    Returns:
    A tuple (is_safe, safe_sequence) where:
    - is_safe: Boolean indicating if the system is in a safe state.
    - safe_sequence: List of process names in a safe sequence if the state is safe.
    """
    work = available[:]  # Copy of available resources
    finish = [False] * len(processes)  # Track which processes can finish
    safe_sequence = []  # To store the safe sequence

    while len(safe_sequence) < len(processes):
        allocated_process = False
        for i in range(len(processes)):
            if not finish[i]:  # If the process hasn't finished
                # Check if the process's needs can be satisfied with available resources
                if all(need[i][j] <= work[j] for j in range(len(available))):
                    # Simulate allocation
                    for j in range(len(available)):
                        work[j] += allocation[i][j]  # Release allocated resources
                    finish[i] = True
                    safe_sequence.append(processes[i])  # Add to safe sequence
                    allocated_process = True
                    break  # Restart to check from the first process

        if not allocated_process:
            # If no process could be allocated in this iteration, we are in an unsafe state
            return False, []

    return True, safe_sequence


# Driver Code
processes = ['P1', 'P2', 'P3', 'P4', 'P5']
available = [3, 2, 2]
allocation = [
    [1, 2, 2],
    [2, 0, 1],
    [1, 1, 1],
    [2, 1, 0],
    [0, 0, 2]
]
maximum = [
    [1, 2, 2],
    [2, 0, 1],
    [1, 1, 1],
    [2, 1, 0],
    [0, 0, 2]
]
# Calculate need matrix
need = [[maximum[i][j] - allocation[i][j] for j in range(len(available))] for i in range(len(processes))]

# Check for safe state
is_safe, safe_sequence = is_safe_state(processes, available, allocation, need)
if is_safe:
    print("The system is in a safe state.")
    print("Safe sequence:", safe_sequence)
else:
    print("The system is in an unsafe state. Deadlock may occur.")
