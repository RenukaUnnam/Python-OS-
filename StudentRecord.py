''' Managing Student Records in a School Database
You are tasked with designing a file management system for a school's student database. The database
contains records of students' personal information, academic performance, and attendance history. Each
student record is stored as a file with specific attributes.
Implement the Sequential File Allocation strategy to manage the storage and access of student records in
the school database.
Here's the scenario of the school database system:
The school has records for three students:
Student A: John Doe, ID 101, Grade 10, Address: 123 Main Street
Student B: Jane Smith, ID 102, Grade 11, Address: 456 Elm Street
Student C: Michael Brown, ID 103, Grade 9, Address: 789 Oak Avenue
Implement and simulate the Sequential File Allocation strategy for storing and accessing these student
records in the school database.
'''
class StudentRecord:
    def __init__(self, name, student_id, grade, address):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"


class SequentialFileAllocation:
    def __init__(self, block_size):
        self.disk_blocks = []
        self.fat = {}
        self.block_size = block_size
        self.next_free_block = 0

    def add_record(self, student_record):
        record_size = self.calculate_record_size(student_record)
        if self.next_free_block >= len(self.disk_blocks):
            self.disk_blocks.append([""] * self.block_size)

        block_index = self.next_free_block
        block = self.disk_blocks[block_index]
        block[0] = student_record
        self.fat[student_record.student_id] = block_index
        self.next_free_block += 1
        return True

    def get_record(self, student_id):
        block_index = self.fat.get(student_id)
        if block_index is None:
            return None

        block = self.disk_blocks[block_index]
        for record in block:
            if isinstance(record, StudentRecord) and record.student_id == student_id:
                return record
        return None

    def calculate_record_size(self, student_record):
        return 1  # Assuming each record takes 1 block for simplicity

    def print_disk_status(self):
        print("Disk Status:")
        for index, block in enumerate(self.disk_blocks):
            print(f"Block {index}:")
            for record in block:
                if isinstance(record, StudentRecord):
                    print(f"  {record}")
                else:
                    print("  Empty")
        print(f"Next free block: {self.next_free_block}")


# Setting up block size and initializing file system
block_size = 1
file_system = SequentialFileAllocation(block_size)

# Creating some student records
student_records = [
    StudentRecord("John Doe", 101, 10, "123 Main Street"),
    StudentRecord("Jane Smith", 102, 11, "456 Elm Street"),
    StudentRecord("Michael Brown", 103, 9, "789 Oak Avenue")
]

# Adding records to the file system
for record in student_records:
    file_system.add_record(record)

# Printing disk status
file_system.print_disk_status()

# Retrieving a record
student_id = 101
retrieved_record = file_system.get_record(student_id)

if retrieved_record:
    print(f"\nRetrieved Record for ID {student_id}:")
    print(retrieved_record)
else:
    print(f"\nRecord with ID {student_id} not found.")
