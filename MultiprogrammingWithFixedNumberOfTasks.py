'''Multiprogramming with a Fixed Number of Tasks (MFT)
You are a systems engineer working on a legacy mainframe system that employs the MFT memory
management technique. The system is designed to handle multiple processes simultaneously by dividing
memory into fixed-size partitions, each capable of holding a single process.
Your mainframe system has a total of 6400 KB of memory available, divided into fixed-size partitions.
Processes of varying sizes are submitted to the system for execution, each requiring a specific amount of
memory. Your task is to implement and simulate the MFT memory management technique to efficiently
allocate memory partitions to these processes.
Memory Partitions: The system memory is divided into fixed-size partitions to accommodate processes.
Partition Size: 800 KB each.
Total Partitions: 8 partitions in total'''

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
