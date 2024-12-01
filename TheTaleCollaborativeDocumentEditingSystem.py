'''The Tale of the Collaborative Document Editing System
Imagine a collaborative document editing platform called EditTogether. This platform allows multiple users
to edit the same document simultaneously. To maintain consistency and prevent conflicts, the system must
manage concurrent access to the document's content effectively.
The Problem: EditTogether needs to handle:
Concurrent Edits: Multiple users might edit the same part of the document at the same time.
Data Integrity: Ensure that all changes are accurately recorded and that no edits are lost or overwritten
improperly.
EditTogether operates with:
• Documents: Users can open and edit shared documents.
• Editors: Each user acts as an editor who can make changes to the document.
'''

import threading
import time
import random

class Document:
    def __init__(self, num_lines=10):
        # Create document with num_lines and a lock for each line
        self.lines = [f"Line {i + 1}: [Empty]" for i in range(num_lines)]
        self.locks = [threading.Lock() for _ in range(num_lines)]

    def edit_line(self, line_number, new_text, user_id):
        if 0 <= line_number < len(self.lines):  # Ensure the line number is valid
            with self.locks[line_number]:
                print(f"{user_id} is editing Line {line_number + 1}")
                time.sleep(random.uniform(0.1, 0.5))  # Simulate editing time
                self.lines[line_number] = f"Line {line_number + 1}: {new_text} (edited by {user_id})"
                print(f"{user_id} completed editing Line {line_number + 1}")
        else:
            print(f"{user_id} attempted to edit invalid Line {line_number + 1}")

    def show_document(self):
        print("\n--- Document Content ---")
        for line in self.lines:
            print(line)
        print("------------------------")

def user_edit(document, user_id):
    for _ in range(3):  # Each user makes 3 edits
        line_number = random.randint(0, len(document.lines) - 1)
        new_text = f"New text by {user_id}"
        document.edit_line(line_number, new_text, user_id)

# Driver Code
document = Document(num_lines=10)  # Create a document with 10 lines
threads = []
user_ids = [f'User{i + 1}' for i in range(10)]  # 10 users

for user_id in user_ids:
    t = threading.Thread(target=user_edit, args=(document, user_id))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

document.show_document()  # Show the final content of the document
print("All user edits completed.")
