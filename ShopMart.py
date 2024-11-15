'''ShopMart
In a bustling online shopping platform, ShopMart, which manages a vast inventory of products and
customer transactions, efficient memory management is crucial to ensure smooth operations and timely
access to product data. ShopMart employs the paging technique to manage memory across its servers.
ShopMart operates multiple servers to handle customer orders and manage product information. Each
server has a total of 512 pages of main memory, and each page can store a fixed amount of product data.
Throughout a busy day of operations, different parts of ShopMart's system make memory requests in the
following sequence:
Product Catalog Management requests 80 pages.
Order Processing System requests 120 pages.
Customer Database requests 150 pages.
Payment Processing Gateway requests 100 pages.
Inventory Tracking System requests 60 pages.
Assume that the memory is initially empty, and all requests arrive sequentially without any memory being
released in between.'''

class Page: 
    def __init__(self, page_id, process_name=None): 
        self.page_id = page_id
        self.process_name = process_name  # None if the page is unallocated
    def allocate(self, process_name): 
        self.process_name = process_name
    def deallocate(self): 
        self.process_name = None
    def __str__(self): 
        if self.process_name:
            return f"Page {self.page_id} | {self.process_name}"
        else:
            return f"Page {self.page_id} | Free"
class MemoryManager: 
    def __init__(self, num_pages, page_size): 
        self.num_pages = num_pages 
        self.page_size = page_size 
        self.pages = [Page(page_id) for page_id in range(num_pages)]
    def allocate_memory(self, process_name, num_pages_requested): 
        free_pages = [page for page in self.pages   if page.process_name is None]
        if len(free_pages) >= num_pages_requested:
            for i in range(num_pages_requested):
                free_pages[i].allocate(process_name)
            return True
        return False
    def print_memory_status(self): 
        for page in self.pages:
            print(page)
        print()  # Blank line for readability
    def print_total_memory_used(self): 
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory_used = used_pages * self.page_size
        print(f"Total memory used: {total_memory_used} units out of {self.num_pages * self.page_size} units\n")
memory_manager = MemoryManager(num_pages=512, page_size=1)
requests = [ 
    ("Product Catalog Management", 80), 
    ("Order Processing System", 120), 
    ("Customer Database", 150), 
    ("Payment Processing Gateway", 100), 
    ("Inventory Tracking System", 60) 
]
for request in requests: 
    process_name, num_pages_requested = request 
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated: 
        print(f"Allocated {num_pages_requested} pages for {process_name}") 
        memory_manager.print_memory_status()
    else: 
        print(f"Not enough memory available for {process_name} (requested {num_pages_requested} pages)\n")
memory_manager.print_total_memory_used()
