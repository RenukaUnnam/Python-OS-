'''AI Lab
In a research institute focused on artificial intelligence (AI) advancements, the AI Lab manages its
computational resources using a first-fit contiguous memory allocation technique. The AI Lab is responsible
for running various experiments and simulations, each requiring different amounts of memory. The AI Lab
operates with a total of 6000 units of memory. Throughout the day, it receives memory requests from
different research projects in the following sequence:
Project A requests 1500 units of memory.
Project B requests 1000 units of memory.
Project C requests 700 units of memory.
Project D requests 2200 units of memory.
Project E requests 500 units of memory.
Project F requests 1200 units of memory.
Assume that the memory is initially empty, and all requests arrive sequentially without any memory being
released in between.'''

class MFTMemoryManager:
    def __init__(self, num_partitions, partition_size):
        self.num_partitions = num_partitions
        self.partition_size = partition_size
        self.available_partitions = [True] * num_partitions
        self.processes = {}

    def allocate_memory(self, process_id, size):
        if size > self.partition_size:
            print(f"Process {process_id} request for {size} KB rejected: Size exceeds partition size.")
            return
        for i in range(self.num_partitions):
            if self.available_partitions[i]:
                self.available_partitions[i] = False
                self.processes[process_id] = i
                print(f"Allocated {size} KB to Process {process_id} in Partition {i + 1}.")
                return
        print(f"Process {process_id} request for {size} KB rejected: No available partition.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_index = self.processes.pop(process_id)
            self.available_partitions[partition_index] = True
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for pid, partition_index in self.processes.items():
            print(f"Process {pid}: allocated in Partition {partition_index + 1}.")
        print("Available Partitions:", [i + 1 for i, available in enumerate(self.available_partitions) if available])

# Driver Code
memory_manager = MFTMemoryManager(num_partitions=8, partition_size=800) 
memory_manager.allocate_memory(1, 600) 
memory_manager.allocate_memory(2, 900) 
memory_manager.allocate_memory(3, 400) 
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
