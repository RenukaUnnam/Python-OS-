'''DigitalArchive
You are a software engineer working for a digital library company called "DigitalArchive". DigitalArchive
specializes in storing and managing vast collections of digital media files for various clients, including
museums, libraries, and private collectors. Your task is to design a file allocation strategy that efficiently
manages these files on DigitalArchive's storage system.
DigitalArchive has recently signed a contract with a renowned museum that wants to digitize and archive
its extensive collection of historical photographs. The museum's collection includes thousands of
photographs ranging from early 20th-century portraits to landscapes and architectural images.
Requirements:
File Types: Each photograph is stored as a digital image file (e.g., JPG format).
File Sizes: The sizes of photographs vary, with average file sizes ranging from 5 MB to 20 MB.
Storage System: DigitalArchive uses a storage system that organizes files into blocks of fixed size (e.g., 10
MB per block).
File Allocation Strategy: Sequential File Allocation'''

class DigitalArchive:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk_blocks = [False] * total_blocks  # False means block is free
        self.file_allocations = {}  # Maps file_name to (start_block, size)

    def allocate_blocks(self, file_name, file_size):
        blocks_needed = self.calculate_blocks_needed(file_size)
        start_block = -1
        free_blocks_count = 0

        for i in range(self.total_blocks):
            if not self.disk_blocks[i]:
                if start_block == -1:
                    start_block = i
                free_blocks_count += 1
                if free_blocks_count == blocks_needed:
                    # Allocate the blocks
                    for j in range(start_block, start_block + blocks_needed):
                        self.disk_blocks[j] = True
                    self.file_allocations[file_name] = (start_block, blocks_needed)
                    return True
            else:
                start_block = -1
                free_blocks_count = 0
        
        return False  # Not enough contiguous blocks available

    def delete_file(self, file_name):
        if file_name in self.file_allocations:
            start_block, size = self.file_allocations[file_name]
            for i in range(start_block, start_block + size):
                self.disk_blocks[i] = False
            del self.file_allocations[file_name]
        else:
            print(f"File {file_name} not found.")

    def calculate_blocks_needed(self, file_size):
        return file_size  # Each block is 1 unit, so file_size is the number of blocks needed

    def display_allocation_status(self):
        allocation_status = ['Free' if not block else 'Allocated' for block in self.disk_blocks]
        status_string = ''.join([f"{i:02d}:{status} | " for i, status in enumerate(allocation_status)])
        print(f"Disk Block Status:\n{status_string}")


# Initialize the DigitalArchive with 100 blocks
digital_archive = DigitalArchive(100)

# Allocate blocks for various files
digital_archive.allocate_blocks("Portrait1.jpg", 15)
digital_archive.allocate_blocks("Landscape1.jpg", 10)
digital_archive.allocate_blocks("Architecture1.jpg", 7)

# Display the current allocation status
print("Current Allocation Status:")
digital_archive.display_allocation_status()

# Delete the "Landscape1.jpg" file
digital_archive.delete_file("Landscape1.jpg")
print("\nAfter deleting Landscape1.jpg:")
digital_archive.display_allocation_status()
