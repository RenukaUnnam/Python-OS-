'''Simulating Paging Memory Management
You are a software engineer tasked with implementing memory management for a new operating system
that utilizes the Paging technique. Paging divides the physical memory into fixed-size blocks (pages) and
manages processes by allocating these pages dynamically.
Your operating system has a total of 4000 KB of physical memory available, divided into fixed-size pages.
Processes of varying sizes are submitted to the system for execution, each requiring a specific amount of
memory. Your task is to implement and simulate the Paging memory management technique to efficiently
allocate memory pages to these processes.
Memory Pages: The system memory is divided into fixed-size pages to accommodate processes.
Page Size: 200 KB each.
Total Pages: 20 pages in total.'''

class PagingMemoryManager:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.available_pages = [True] * num_pages
        self.processes = {}

    def allocate_memory(self, process_id, size):
        num_pages_needed = (size + self.page_size - 1) // self.page_size  # Round up to nearest page
        pages_allocated = []

        for i in range(self.num_pages):
            if self.available_pages[i]:
                pages_allocated.append(i)
                if len(pages_allocated) == num_pages_needed:
                    break

        if len(pages_allocated) == num_pages_needed:
            for page in pages_allocated:
                self.available_pages[page] = False
            self.processes[process_id] = pages_allocated
            print(f"Allocated {size} KB to Process {process_id} using pages {pages_allocated}.")
        else:
            print(f"Process {process_id} request for {size} KB rejected: Not enough available pages.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            for page in self.processes.pop(process_id):
                self.available_pages[page] = True
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for pid, pages in self.processes.items():
            print(f"Process {pid}: allocated pages {pages}.")
        print("Available Pages:", [i for i, available in enumerate(self.available_pages) if available])

# Driver Code
memory_manager = PagingMemoryManager(num_pages=20, page_size=200) 
memory_manager.allocate_memory(1, 400) 
memory_manager.allocate_memory(2, 600) 
memory_manager.allocate_memory(3, 300) 
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
