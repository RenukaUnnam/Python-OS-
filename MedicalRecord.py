'''Managing Medical Records in a Hospital Information System
You have been tasked with designing a file management system for a hospital's electronic medical records
(EMR). The EMR system contains detailed records of patients' medical histories, treatments, and diagnostic
results. Each patient record is stored as a file with specific attributes.
Implement the Indexed File Allocation strategy to efficiently manage the storage and access of patient
records in the hospital's EMR system.
Here's the scenario of the hospital information system:
The hospital manages records for several patients:
Patient A: John Smith, Age 45, Medical ID 1001, Address: 123 Hospital Road
Patient B: Jane Doe, Age 32, Medical ID 1002, Address: 456 Clinic Avenue
Patient C: Michael Johnson, Age 58, Medical ID 1003, Address: 789 Medical Plaza
Implement and simulate the Indexed File Allocation strategy for storing and accessing these patient records
in the hospital's EMR system.'''

class PatientRecord:
    def __init__(self, name, age, medical_id, address):
        self.name = name
        self.age = age
        self.medical_id = medical_id
        self.address = address

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Medical ID: {self.medical_id}, "
                f"Address: {self.address}")


class IndexedFileAllocation:
    def __init__(self, block_size):
        self.disk_blocks = []  # List to simulate disk blocks
        self.index_table = {}  # Index table: maps medical_id to disk block index and record index
        self.index_block_size = block_size
        self.next_free_block = 0

    def add_record(self, patient_record):
        record_size = self.calculate_record_size(patient_record)
        if self.next_free_block >= len(self.disk_blocks):
            self.disk_blocks.append([None] * self.index_block_size)

        block_index = len(self.disk_blocks) - 1
        block = self.disk_blocks[block_index]
        for i in range(self.index_block_size):
            if block[i] is None:
                block[i] = patient_record
                self.index_table[patient_record.medical_id] = (block_index, i)
                return True

        # If block is full, create a new block and recursively add the record
        self.disk_blocks.append([None] * self.index_block_size)
        self.next_free_block += 1
        return self.add_record(patient_record)  # Recursive call to place the record in the new block

    def get_record(self, medical_id):
        if medical_id in self.index_table:
            block_index, record_index = self.index_table[medical_id]
            block = self.disk_blocks[block_index]
            return block[record_index]
        return None

    def calculate_record_size(self, patient_record):
        return 1  # Assuming each record takes 1 slot/block for simplicity

    def print_disk_status(self):
        print("Disk Status:")
        for i, block in enumerate(self.disk_blocks):
            print(f"Block {i}:")
            for record in block:
                if record is not None:
                    print(f"  {record}")
                else:
                    print("  [Empty]")


# Setting up block size and initializing file system
index_block_size = 1
file_system = IndexedFileAllocation(index_block_size)

# Creating some patient records
patient_records = [
    PatientRecord("John Smith", 45, 1001, "123 Hospital Road"),
    PatientRecord("Jane Doe", 32, 1002, "456 Clinic Avenue"),
    PatientRecord("Michael Johnson", 58, 1003, "789 Medical Plaza")
]

# Adding records to the file system
for record in patient_records:
    file_system.add_record(record)

# Printing disk status
file_system.print_disk_status()

# Retrieving a record
medical_id = 1002
retrieved_record = file_system.get_record(medical_id)

if retrieved_record:
    print(f"\nRetrieved Record for Medical ID {medical_id}:")
    print(retrieved_record)
else:
    print(f"\nRecord with Medical ID {medical_id} not found.")
