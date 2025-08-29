
transactions = [
    {"id": 1, "amount": 200, "type": "deposit"},
    {"id": 2, "amount": 50, "type": "withdraw"},
    {"id": 3, "amount": 500, "type": "deposit"}
]

def filter_transactions(transactions, criteria):
	found = []
	for transaction in transactions:
		for key, value in criteria.items():
			if type(value) == int:
				if transaction[key] > value:
					found.append(transaction)
			elif type(value) == str:
				if transaction[key] == value: 
					found.append(transaction)
		
	if found:
		return found
	else:
		return "Not found"
				


criteria = {'type': 'withdraw' }
print(filter_transactions(transactions, criteria))
