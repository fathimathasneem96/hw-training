import csv
import json

# Input and output file paths
csv_file = 'sample_data.csv'
json_file = 'data.json'

# Read CSV and convert to list of dicts
with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Write to JSON
with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("CSV converted to JSON successfully.")
