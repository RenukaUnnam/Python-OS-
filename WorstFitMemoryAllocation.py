'''Worst Fit Memory Allocation
You are a system analyst tasked with designing memory management techniques for a new operating
system. One of the techniques to implement is the Worst Fit memory allocation algorithm, which prioritizes
allocating the largest available memory block to processes.
Your operating system is designed to manage a system with a total of 1200 KB of memory available, divided
into fixed-size memory blocks. Processes of varying sizes are submitted to the system for execution, each
requiring a specific amount of memory. Your task is to implement and simulate the Worst Fit memory
allocation algorithm to efficiently allocate memory blocks to these processes.
Memory Blocks: The system has a total of 10 memory blocks available, each with a fixed size.
Block 1: 150 KB
Block 2: 300 KB
Block 3: 100 KB
Block 4: 200 KB
Block 5: 250 KB
Block 6: 50 KB
Block 7: 350 KB
Block 8: 180 KB
Block 9: 120 KB
Block 10: 200 KB'''

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
