'''CentralAI
In a futuristic city where advanced artificial intelligence (AI) systems govern public services, a central AI hub
named CentralAI operates using a sophisticated memory management system. CentralAI oversees various
subsystems, each requiring different amounts of memory to function efficiently. To optimize its memory
usage, CentralAI employs the best-fit contiguous memory allocation technique. CentralAI manages a total
of 8000 units of memory. Throughout the day, it receives memory requests from different subsystems in
the following sequence:
SubsysA requests 1500 units of memory.
SubsysB requests 1000 units of memory.
SubsysC requests 700 units of memory.
SubsysD requests 2200 units of memory.
SubsysE requests 500 units of memory.
SubsysF requests 1200 units of memory.
Assume that the memory is initially empty, and all requests arrive sequentially without any memory being
released in between'''
class BestFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.available_blocks = {i: block for i, block in enumerate(memory_blocks)}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        best_fit_index = None
        for i, block in self.available_blocks.items():
            if block >= size and (best_fit_index is None or block < self.available_blocks[best_fit_index]):
                best_fit_index = i

        if best_fit_index is not None:
            self.processes[process_id] = self.available_blocks[best_fit_index]
            del self.available_blocks[best_fit_index]
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
memory_manager = BestFitMemoryManager([100, 200, 50, 150, 300, 80, 120, 200]) 
memory_manager.allocate_memory(1, 70) 
memory_manager.allocate_memory(2, 180) 
memory_manager.allocate_memory(3, 250)
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
