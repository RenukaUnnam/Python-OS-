''' The Tale of the Bank Account Management System
Imagine a large bank called SecureBank that handles thousands of transactions every day. The bank uses
an automated system to manage customer accounts. The system must ensure that transactions are
processed accurately and that account balances are correctly updated even when multiple transactions
occur simultaneously.
SecureBank needs to handle:
• Concurrent Transactions: Multiple transactions may be processed on the same account at the
same time.
• Data Integrity: Ensure that account balances are updated correctly and that no transactions are
lost or incorrectly applied.
SecureBank operates with:
• Accounts: Each customer has a unique account with a balance.
• Transactions: Transactions include deposits and withdrawals that modify account balances.
'''

import threading
import time
import random

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Depositing {amount}...")
            time.sleep(random.uniform(0.1, 0.3))  # Simulate processing delay
            self.balance += amount
            print(f"Deposit of {amount} completed. New balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}...")
                time.sleep(random.uniform(0.1, 0.3))  # Simulate processing delay
                self.balance -= amount
                print(f"Withdrawal of {amount} completed. New balance: {self.balance}")
            else:
                print(f"Withdrawal of {amount} failed. Insufficient balance. Current balance: {self.balance}")

def perform_transaction(account, transaction_type, amount):
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        account.withdraw(amount)

# Driver Code
account = BankAccount(balance=1000)
threads = []
transaction_types = ['deposit', 'withdraw']

for _ in range(20):  # 20 transactions
    transaction_type = random.choice(transaction_types)
    amount = random.randint(50, 200)  # Random amount between 50 and 200
    t = threading.Thread(target=perform_transaction, args=(account, transaction_type, amount))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"All transactions completed. Final account balance: {account.balance}")
