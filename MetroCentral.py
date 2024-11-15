''' MetroCentral
In a bustling metropolis where a central command center, MetroCentral, manages all public transportation
systems using advanced computer systems, efficient memory management is critical. MetroCentral employs
the first-fit contiguous memory allocation technique to handle memory requests from various subsystems
that control different aspects of the transportation network. MetroCentral operates with a total of 5000
units of memory. Throughout the day, it receives memory requests from different subsystems in the
following sequence:
TrafficControl requests 1200 units of memory.
RoutePlanning requests 800 units of memory.
VehicleMonitoring requests 1500 units of memory.
PassengerInformation requests 600 units of memory.
MaintenanceLogistics requests 700 units of memory.
Assume that the memory is initially empty, and all requests arrive sequentially without any memory being
released in between.
'''
class WorstFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.available_blocks = {i: block for i, block in enumerate(memory_blocks)}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        worst_fit_index = None
        for i, block in self.available_blocks.items():
            if block >= size and (worst_fit_index is None or block > self.available_blocks[worst_fit_index]):
                worst_fit_index = i

        if worst_fit_index is not None:
            self.processes[process_id] = self.available_blocks[worst_fit_index]
            del self.available_blocks[worst_fit_index]
            print(f"Allocated {size} KB to Process {process_id}.")
        else:
            print(f"Process {process_id} request for {size} KB rejected: No suitable block found.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            block_size = self.processes.pop(process_id)
            self.available_blocks[len(self.available_blocks)] = block_size
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for pid, size in self.processes.items():
            print(f"Process {pid}: {size} KB allocated.")
        print("Available Memory Blocks:", sorted(self.available_blocks.values()))

# Driver Code
memory_manager = WorstFitMemoryManager([150, 300, 100, 200, 250, 50, 350, 180, 120, 200]) 
memory_manager.allocate_memory(1, 180) 
memory_manager.allocate_memory(2, 400) 
memory_manager.allocate_memory(3, 120) 
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
