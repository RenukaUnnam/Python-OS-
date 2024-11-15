'''Best Fit Memory Allocation
You are a software developer working on an operating system project that requires implementing memory
management techniques. One of the critical components is the Best Fit memory allocation algorithm, which
aims to allocate memory blocks to processes in a way that minimizes wastage and fragmentation.
Page | 26
Your operating system is designed to manage a system with a total of 800 KB of memory available.
Processes of varying sizes are submitted to the system for execution, each requiring a specific amount of
memory. Your task is to implement and simulate the Best Fit memory allocation algorithm to efficiently
allocate memory blocks to these processes.
Memory Blocks: The system has a total of 8 memory blocks available, each with a fixed size.
Block 1: 100 KB
Block 2: 200 KB
Block 3: 50 KB
Block 4: 150 KB
Block 5: 300 KB
Block 6: 80 KB
Block 7: 120 KB
Block 8: 200 KB'''

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
