''' Managing Digital Media Files in a Multimedia Application
You are developing a multimedia application that allows users to manage and store various types of digital
media files, including images, videos, and audio clips. Each file is treated as a separate entity with its own
attributes and content.
Implement the Linked File Allocation strategy to efficiently manage the storage and access of digital media
files in your multimedia application.
Here's the scenario of the multimedia application:
The application needs to manage the following digital media files:
File A: Landscape.jpg (Image file), size 5 MB
File B: Concert.mp4 (Video file), size 50 MB
File C: Song.mp3 (Audio file), size 8 MB
Implement and simulate the Linked File Allocation strategy for storing and accessing these digital media
files in the multimedia application.'''

from random import randint, choice

class DiskBlock:
    def __init__(self, block_id):
        self.block_id = block_id
        self.next_block = None  # Initially, no next block is assigned

class MediaFile:
    def __init__(self, file_name, file_type, size):
        self.file_name = file_name
        self.file_type = file_type
        self.size = size
        self.start_block = None  # Points to the first block in the chain

    def __str__(self):
        return f"{self.file_name} ({self.file_type}), Size: {self.size} MB"

class FileAllocationTable:
    def __init__(self):
        self.fat = {}  # Maps block_id to the next block_id in the chain

    def allocate_blocks(self, media_file, disk_blocks):
        available_blocks = [block for block in disk_blocks if block.next_block is None]
        
        if len(available_blocks) < media_file.size:
            raise ValueError("Not enough disk blocks available to allocate.")
        
        first_block = available_blocks[0]
        media_file.start_block = first_block
        self.fat[first_block.block_id] = None  # Initialize FAT entry for the first block
        previous_block = first_block
        
        for i in range(1, media_file.size):
            current_block = available_blocks[i]
            self.fat[previous_block.block_id] = current_block.block_id
            previous_block.next_block = current_block
            self.fat[current_block.block_id] = None  # Initialize FAT entry for the current block
            previous_block = current_block
        
        self.fat[previous_block.block_id] = None  # Last block points to None
        previous_block.next_block = None

    def delete_file(self, media_file, disk_blocks):
        current_block = media_file.start_block
        while current_block:
            next_block = current_block.next_block
            self.fat.pop(current_block.block_id, None)  # Remove block from FAT
            current_block.next_block = None  # Clear the link to the next block
            current_block = next_block
        media_file.start_block = None

def simulate_linked_file_allocation():
    # Create disk blocks
    disk_blocks = [DiskBlock(block_id) for block_id in range(10)]
    fat = FileAllocationTable()
    media_files = [
        MediaFile("Movie1", "MP4", 3),
        MediaFile("Song1", "MP3", 2),
        MediaFile("Document1", "PDF", 1)
    ]
    
    # Allocate blocks for each media file
    for file in media_files:
        try:
            fat.allocate_blocks(file, disk_blocks)
            print(f"Allocated blocks for {file}")
        except ValueError as e:
            print(e)
    
    print("\nDisk Blocks Allocation:")
    for block in disk_blocks:
        next_block_id = block.next_block.block_id if block.next_block else None
        print(f"Block {block.block_id} -> Next Block: {next_block_id}")
    
    # Delete "Song1"
    file_to_delete = media_files[1]  # Delete "Song1"
    fat.delete_file(file_to_delete, disk_blocks)
    print(f"\nDeleted file: {file_to_delete}")
    
    print("\nDisk Blocks Allocation After Deletion:")
    for block in disk_blocks:
        next_block_id = block.next_block.block_id if block.next_block else None
        print(f"Block {block.block_id} -> Next Block: {next_block_id}")

simulate_linked_file_allocation()
