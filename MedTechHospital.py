'''MedTech Hospital
In a bustling city where a central hospital, MedTech Hospital, manages its patient records and medical data
using sophisticated computer systems, efficient memory management is crucial. MedTech Hospital employs
the best-fit contiguous memory allocation technique to optimize its use of memory resources. MedTech
Hospital operates with a total of 8000 units of memory. Throughout a busy day, it receives memory requests
from different departments and systems in the following sequence:
Emergency Department requests 2000 units of memory.
Cardiology Department requests 1500 units of memory.
Laboratory Information System requests 1200 units of memory.
Radiology Department requests 1800 units of memory.
Patient Management System requests 1000 units of memory.
Pharmacy System requests 600 units of memory.
Surgical Services requests 2200 units of memory.
Page | 39
Assume that the memory is initially empty, and all requests arrive sequentially without any memory being
released in between.'''

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
