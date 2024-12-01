'''UrbanOS - Wait-for-Graph (WFG)
UrbanOS, a sophisticated operating system powering a smart city, relies on efficient process management
and dependency tracking to ensure seamless operations across its diverse infrastructure. One of the key
mechanisms UrbanOS utilizes is the Wait-for-Graph (WFG), which helps manage dependencies and prevent
potential deadlock situations among concurrent processes.
Process and Task Management:
UrbanOS oversees a myriad of critical processes that operate simultaneously to support city functions:
Process A: Manages real-time traffic signal adjustments at intersections.
Process B: Handles data aggregation and analytics for environmental sensors.
Process C: Coordinates emergency response dispatch and resource allocation.
Process D: Facilitates centralized billing and utility management.
Concurrency and Dependency Dynamics:
Each process in UrbanOS may depend on resources such as CPU time, memory, network access, and access
to shared databases or sensors. Processes dynamically interact, requesting resources and potentially waiting
for others to release resources before proceeding.
'''

class Process:
    def __init__(self, pid):
        self.pid = pid  # Process ID
        self.dependencies = set()  # Set of processes this process is waiting for

    def add_dependency(self, process):
        self.dependencies.add(process)

    def remove_dependency(self, process):
        self.dependencies.discard(process)

    def __str__(self):
        return f"Process {self.pid}: Waiting for {[p.pid for p in self.dependencies]}"


class WaitForGraph:
    def __init__(self):
        self.processes = {}  # Dictionary to store processes by their PID

    def add_process(self, process):
        self.processes[process.pid] = process

    def add_dependency(self, process_pid, dependency_pid):
        process = self.processes.get(process_pid)
        dependency = self.processes.get(dependency_pid)
        if process and dependency:
            process.add_dependency(dependency)

    def remove_dependency(self, process_pid, dependency_pid):
        process = self.processes.get(process_pid)
        dependency = self.processes.get(dependency_pid)
        if process and dependency:
            process.remove_dependency(dependency)

    def detect_deadlocks(self):
        visited = set()
        recursion_stack = set()

        def detect_cycle(process):
            if process in recursion_stack:
                return True
            if process in visited:
                return False

            visited.add(process)
            recursion_stack.add(process)
            for dependency in process.dependencies:
                if detect_cycle(dependency):
                    return True
            recursion_stack.remove(process)
            return False

        for process in self.processes.values():
            if detect_cycle(process):
                return True
        return False

    def print_wfg(self):
        print("Wait-For Graph:")
        for process in self.processes.values():
            print(process)


# Driver Code
process1 = Process(1)
process2 = Process(2)
process3 = Process(3)
process4 = Process(4)

wfg = WaitForGraph()

# Adding processes to the graph
wfg.add_process(process1)
wfg.add_process(process2)
wfg.add_process(process3)
wfg.add_process(process4)

# Adding dependencies
wfg.add_dependency(1, 2)
wfg.add_dependency(2, 3)
wfg.add_dependency(3, 4)
wfg.add_dependency(4, 1)  # Creates a cycle

# Print the WFG
wfg.print_wfg()

# Detect and resolve deadlocks
if wfg.detect_deadlocks():
    print("Deadlock detected in the system.")
    wfg.remove_dependency(4, 1)  # Resolving the deadlock by removing a dependency
    print("Deadlock resolved.")
else:
    print("No deadlock detected.")

# Print the updated WFG
wfg.print_wfg()
