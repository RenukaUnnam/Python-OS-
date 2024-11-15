'''GameTech Studios
In a bustling gaming company, GameTech Studios, which hosts multiplayer online games, efficient memory
management is crucial to ensure seamless gameplay experiences for millions of players worldwide.
GameTech Studios employs the paging technique to manage memory across its gaming servers. GameTech
Studios operates multiple gaming servers, each equipped with a paging system. The main memory of each
server is divided into fixed-size pages, and game sessions running on these servers request memory in
terms of these pages. Each page can store a fixed amount of game data.
Each gaming server has a total of 256 pages of main memory.
Each page can hold up to 16 units of game data.
Throughout a peak gaming period, several game sessions make memory requests in the following
sequence:
Page | 45
Game Session 1 requests 32 pages.
Game Session 2 requests 20 pages.
Game Session 3 requests 40 pages.
Game Session 4 requests 18 pages.
Game Session 5 requests 25 pages.
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
        free_pages = [page for page in self.pages if page.process_name is None]
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
memory_manager = MemoryManager(num_pages=256, page_size=16)
requests = [ 
        ("Game Session 1", 32), 
        ("Game Session 2", 20), 
        ("Game Session 3", 40), 
        ("Game Session 4", 18), 
        ("Game Session 5", 25) 
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
