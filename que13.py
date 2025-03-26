sample_data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}


highest=0
highest_key=""
for key in sample_data:
    if sample_data[key]>highest:
        highest=sample_data[key]
        highest_key=key

print(highest_key +":",highest)
sample_data.pop(highest_key)

highest=0
highest_key=""
for key in sample_data:
    if sample_data[key]>highest:
        highest=sample_data[key]
        highest_key=key

print(highest_key +":",highest)
sample_data.pop(highest_key)
highest=0
highest_key=""
for key in sample_data:
    if sample_data[key]>highest:
        highest=sample_data[key]
        highest_key=key

print(highest_key +":",highest)
sample_data.pop(highest_key)