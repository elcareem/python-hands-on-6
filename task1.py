
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
		for i in found:
			print(i)
	else:
		print("Not found")
				


criteria = {'amount': 100}
filter_transactions(transactions, criteria)
