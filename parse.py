import json

with open('stack_overflow_1.json') as data_file:
	data = json.load(data_file)
	
	
print(data['node1'])
print();
print(len(data['node1']))
print(len(data))