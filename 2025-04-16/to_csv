import json
import csv

# Input and output file paths
json_file = 'data.json'
csv_file = 'data.csv'

# Read JSON data
with open(json_file, mode='r', encoding='utf-8') as f:
    data = json.load(f)

# Write CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully.")
