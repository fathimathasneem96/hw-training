import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('haraj_ksa_2024_01.json',lines=True)

#print first 10 urls for viewing
print(df["url"].head(10))

#display urls as text file
df["url"].to_csv("urls_output.txt", index=False, header=False)

#define URL pattern
url_pattern = re.compile(r'^https?://haraj\.com\.sa/\d+/.+$')

#apply regex to validate each URL
df['is_valid_url'] = df['url'].apply(lambda x: bool(url_pattern.match(str(x))))

#save invalid URLs for review
invalid_urls = df[~df['is_valid_url']]
invalid_urls.to_csv('invalid_urls.csv', index=False)

#print number of records checked and records with invalid urls
print(f"Checked {len(df)} records. Found {len(invalid_urls)} invalid URLs.")



Output: 
0    https://haraj.com.sa/11128073101/Ground_floor_...
1    https://haraj.com.sa/11127935695/Ground_floor_...
2    https://haraj.com.sa/11127877105/Ground_floor_...
3    https://haraj.com.sa/11127766404/Upper_floor_f...
4    https://haraj.com.sa/11127697284/Ground_floor_...
5      https://haraj.com.sa/11127287669/House_for_rent
6    https://haraj.com.sa/11126994184/Renovated_gro...
7    https://haraj.com.sa/11128019057/Floor_for_ren...
8            https://haraj.com.sa/11128006153/upstairs
9    https://haraj.com.sa/11126795798/An_attached_f...
Name: url, dtype: object
Checked 78828 records. Found 0 invalid URLs.
