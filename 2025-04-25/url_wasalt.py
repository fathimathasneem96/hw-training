import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('wasalt_ksa_2025_05.json',lines=True)

#print first 10 urls for viewing
print(df["url"].head(10))

#display urls as text file
df["url"].to_csv("url_output.txt", index=False, header=False)

#define URL pattern
url_pattern = re.compile(r'^https?://wasalt\.com\/en/.+$')

#apply regex to validate each URL
df['is_valid_url'] = df['url'].apply(lambda x: bool(url_pattern.match(str(x))))

#save invalid URLs for review
invalid_urls = df[~df['is_valid_url']]
invalid_urls.to_csv('invalid_urls.csv', index=False)

#print number of records checked and records with invalid urls
print(f"Checked {len(df)} records. Found {len(invalid_urls)} invalid URLs.")


Output: 
0    https://wasalt.com/en/project/Riyadh/-100259/a...
1    https://wasalt.com/en/project/Riyadh/-100259/a...
2    https://wasalt.com/en/project/Riyadh/-100259/a...
3    https://wasalt.com/en/project/Riyadh/-100259/a...
4    https://wasalt.com/en/project/Riyadh/-100259/a...
5    https://wasalt.com/en/project/Riyadh/-100259/a...
6    https://wasalt.com/en/project/Riyadh/-100259/a...
7    https://wasalt.com/en/project/Riyadh/-100259/a...
8    https://wasalt.com/en/project/Riyadh/-100259/a...
9    https://wasalt.com/en/project/Riyadh/-100259/a...
Name: url, dtype: object
Checked 24701 records. Found 0 invalid URLs.
