'''UrbanOS - Resource Allocation Graph (RAG)
In a bustling city, UrbanOS, which operates a complex multitasking operating system, efficient resource
management is crucial to ensure smooth operation of various processes and applications. UrbanOS employs
a Resource Allocation Graph (RAG) to manage resource allocation and avoid deadlock situations. UrbanOS
manages resources such as CPU time, memory, and peripherals across multiple processes running
concurrently. Each process may request and release different resources dynamically throughout its
execution.
Process Management: UrbanOS supports several processes including:
Process A: Handles user interface interactions and graphics rendering.
Process B: Manages database transactions and file operations.
Process C: Performs complex calculations and simulations.
Process D: Controls network communications and data transfers.
Resource Requests:
Each process in UrbanOS can request multiple resources such as CPU time, memory blocks, and access to
peripherals like printers or network devices. Processes dynamically request resources based on their current
tasks and release them when no longer needed.
Resource Allocation Graph (RAG):
UrbanOS maintains a Resource Allocation Graph (RAG) to track which processes are currently allocated
which resources and which processes are waiting for which resources. The RAG helps UrbanOS detect
potential deadlock scenarios where processes are waiting indefinitely for resources held by others.
'''

class Process:
    def __init__(self, pid, max_resources):
        self.pid = pid  # Process ID
        self.max_resources = max_resources  # Maximum resources the process can request
        self.allocated_resources = {res: 0 for res in max_resources}  # Currently allocated resources

    def request_resource(self, resource, amount):
        if resource in self.max_resources and self.allocated_resources[resource] + amount <= self.max_resources[resource]:
            self.allocated_resources[resource] += amount
            return True
        return False

    def release_resource(self, resource, amount):
        if resource in self.allocated_resources and self.allocated_resources[resource] >= amount:
            self.allocated_resources[resource] -= amount
            return True
        return False

    def __str__(self):
        return f"Process {self.pid}: Max={self.max_resources}, Allocated={self.allocated_resources}"


class ResourceManager:
    def __init__(self, resources):
        self.resources = resources  # Total available resources
        self.available_resources = resources.copy()  # Currently available resources
        self.processes = {}  # Dictionary of processes by their ID

    def add_process(self, process):
        self.processes[process.pid] = process

    def request_resource(self, process_id, resource, amount):
        if resource in self.available_resources and self.available_resources[resource] >= amount:
            process = self.processes.get(process_id)
            if process and process.request_resource(resource, amount):
                self.available_resources[resource] -= amount
                return True
        return False

    def release_resource(self, process_id, resource, amount):
        process = self.processes.get(process_id)
        if process and process.release_resource(resource, amount):
            self.available_resources[resource] += amount
            return True
        return False

    def print_processes_status(self):
        print("Resources:")
        print(f"Available: {self.available_resources}")
        for process in self.processes.values():
            print(process)


# Driver Code
resources = {"CPU": 1, "Memory": 1024}

process1 = Process(1, {"CPU": 1, "Memory": 512})
process2 = Process(2, {"CPU": 1, "Memory": 768})

resource_manager = ResourceManager(resources)
resource_manager.add_process(process1)
resource_manager.add_process(process2)

print("Initial State:")
resource_manager.print_processes_status()

if resource_manager.request_resource(1, "CPU", 1):
    print("Process 1 allocated CPU")
else:
    print("Process 1 failed to allocate CPU")

if resource_manager.request_resource(1, "Memory", 512):
    print("Process 1 allocated Memory")
else:
    print("Process 1 failed to allocate Memory")

resource_manager.print_processes_status()

if resource_manager.request_resource(2, "Memory", 768):
    print("Process 2 allocated Memory")
else:
    print("Process 2 failed to allocate Memory")

resource_manager.print_processes_status()

if resource_manager.release_resource(1, "Memory", 512):
    print("Process 1 released Memory")
else:
    print("Process 1 failed to release Memory")

resource_manager.print_processes_status()
