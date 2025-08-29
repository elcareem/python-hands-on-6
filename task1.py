"""
You are given a list of bank transactions:

transactions = [
    {"id": 1, "amount": 200, "type": "deposit"},
    {"id": 2, "amount": 50, "type": "withdraw"},
    {"id": 3, "amount": 500, "type": "deposit"}
]

function Signature
def filter_transactions(transactions, criteria):
    pass

Requirement(s):
The function should return a list of transactions that match the given criteria.

1. If the criteria is a string field (e.g., "type": "deposit"), return only those transactions with the exact same type.
    filter_transactions(transactions, {"type": "deposit"})
 → Returns all deposit transactions

2.   If the criteria is a numeric field (e.g., "amount": 100), return all transactions where the value is greater than or equal to the given number.

filter_transactions(transactions, {"amount": 100})
 → Returns all transactions with amount ≥ 100


 Expected Output Examples:
print(filter_transactions(transactions, {"type": "deposit"}))
[{'id': 1, 'amount': 200, 'type': 'deposit'},
{'id': 3, 'amount': 500, 'type': 'deposit'}]

print(filter_transactions(transactions, {"amount": 100}))
[{'id': 1, 'amount': 200, 'type': 'deposit'},
{'id': 3, 'amount': 500, 'type': 'deposit'}]

"""
