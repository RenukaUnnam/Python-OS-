'''EnterpriseX
You are a systems engineer working for a large multinational corporation that specializes in developing
operating systems for enterprise-level servers. Your team is tasked with designing a file allocation strategy
that optimizes data access and storage efficiency for the company's new flagship operating system, OS
EnterpriseX.
OS EnterpriseX is designed to handle large-scale data processing and storage for corporate clients. One of
the critical requirements is to efficiently manage and access large files, such as databases and multimedia
content, stored on disk drives. The system needs to ensure quick access to specific data blocks while
maintaining efficient storage utilization.
Requirements:
File Types: Files managed by OS EnterpriseX include database files (structured data) and multimedia files
(e.g., videos, images).
Storage System: The operating system uses a disk storage system divided into blocks of fixed size (e.g., 8
KB per block).'''

class OperatingSystem:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk_blocks = [False] * total_blocks  # False indicates block is free
        self.index = {}  # Maps file names to tuples of (start_block, number_of_blocks)

    def allocate_blocks(self, file_name, file_size):
        blocks_needed = self.calculate_blocks_needed(file_size)
        start_block = self.find_free_blocks(blocks_needed)
        if start_block is not None:
            for i in range(start_block, start_block + blocks_needed):
                self.disk_blocks[i] = True
            self.index[file_name] = (start_block, blocks_needed)
            return True
        else:
            print(f"Not enough contiguous free blocks to allocate '{file_name}'.")
            return False

    def delete_file(self, file_name):
        if file_name in self.index:
            start_block, num_blocks = self.index[file_name]
            for i in range(start_block, start_block + num_blocks):
                self.disk_blocks[i] = False
            del self.index[file_name]
        else:
            print(f"File '{file_name}' not found.")

    def find_free_blocks(self, required_blocks):
        free_blocks_count = 0
        start_block = None
        for i in range(self.total_blocks):
            if not self.disk_blocks[i]:
                if start_block is None:
                    start_block = i
                free_blocks_count += 1
                if free_blocks_count == required_blocks:
                    return start_block
            else:
                start_block = None
                free_blocks_count = 0
        return None

    def calculate_blocks_needed(self, file_size):
        # Assume 1 block per 1 MB of file size
        return file_size

    def total_free_blocks(self):
        return self.disk_blocks.count(False)

    def display_allocation_status(self):
        status = ''.join(['1' if block else '0' for block in self.disk_blocks])
        print("Disk Blocks Allocation:")
        print(status)


# Driver Code
os = OperatingSystem(1000)
os.allocate_blocks("database.db", 300)
os.allocate_blocks("video.mp4", 600)
os.allocate_blocks("image.jpg", 150)

print("Current Allocation Status:")
os.display_allocation_status()

os.delete_file("video.mp4")
print("\nAfter deleting video.mp4:")
os.display_allocation_status()
