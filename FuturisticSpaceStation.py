'''Futuristic Space Station
In a futuristic space station, the central computer manages memory allocation using the worst-fit technique.
The memory is divided into fixed-size blocks, and whenever a program requests memory allocation, the
system searches for the largest available block that can accommodate the program's size. One day, the
space station receives requests from three different programs:
Program A requires 150 units of memory.
Program B requires 300 units of memory.
Program C requires 200 units of memory.
The memory blocks available in the system are as follows:
Block 1: 400 units
Block 2: 250 units
Block 3: 350 units
Block 4: 200 units
Block 5: 150 units
Assume the worst-fit algorithm starts its search from the beginning of the memory and scans sequentially
to find the largest block that fits each program's requirement.
Task: Determine how the worst-fit algorithm assigns memory blocks to each program, and calculate the
remaining memory after all programs are allocated.'''

class MemoryVariableTechnique:
    def __init__(self, partitions):
        self.partitions = partitions
        self.memory_map = {pid: [False] * size for pid, size in partitions.items()}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        suitable_partition = min((pid for pid in self.partitions if self.partitions[pid] >= size), 
                                 key=lambda x: self.partitions[x], default=None)

        if suitable_partition is not None:
            free_blocks = self.memory_map[suitable_partition]
            start_index = next((i for i in range(len(free_blocks) - size + 1) if all(not free_blocks[j] for j in range(i, i + size))), -1)
            if start_index != -1:
                for i in range(start_index, start_index + size):
                    free_blocks[i] = True
                self.processes[process_id] = (suitable_partition, start_index, size)
                print(f"Allocated {size} KB to Process {process_id} in Partition {suitable_partition}.")
            else:
                print(f"Unable to allocate {size} KB to Process {process_id}: Not enough contiguous space.")
        else:
            print(f"Process {process_id} request for {size} KB exceeds available partitions.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_id, start_index, size = self.processes.pop(process_id)
            for i in range(start_index, start_index + size):
                self.memory_map[partition_id][i] = False
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for pid, free_blocks in self.memory_map.items():
            allocated_size = free_blocks.count(True)
            print(f"Partition {pid} ({self.partitions[pid]} KB): {allocated_size} KB allocated, "
                  f"{self.partitions[pid] - allocated_size} KB free.")
        print(f"Active Processes: {self.processes}")

# Driver Code
mvt = MemoryVariableTechnique({1: 300, 2: 500, 3: 200}) 
mvt.allocate_memory(1, 150) 
mvt.allocate_memory(2, 400) 
mvt.allocate_memory(3, 100) 
mvt.display_memory_status()
mvt.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
mvt.display_memory_status()
