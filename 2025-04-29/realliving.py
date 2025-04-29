import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('realliving_realestate_2025_05_05.json',lines=True)

#print first 10 urls for viewing
print(df["profile_url"].head(10))

#display urls as text file
df["profile_url"].to_csv("profile_urls.txt", index=False, header=False)

#define  profile URL pattern
profile_url_pattern = re.compile(r'^https:\/\/www\.realliving(?:realestatesolutions)?\.com\/[a-zA-Z0-9\-._]+$')

#apply regex to validate each profile URL
df['is_valid_profile_url'] = df['profile_url'].apply(lambda x: bool(profile_url_pattern.match(str(x))))

#save invalid profile URLs for review
invalid_profiles = df[~df['is_valid_profile_url']]
invalid_profiles.to_csv('invalid_profiles.csv', index=False)

#print number of records checked and records with invalid profile urls
print(f"Checked {len(df)} records. Found {len(invalid_profiles)} invalid profile URLs.")


#define fields want to check
required_fields = ['title', 'office_name', 'address', 'city', 'state',  'zipcode', 
                  'profile_url', 'languages', 'description', 'first_name', 'middle_name',
                  'last_name', 'website', 'email', 'image_url', 
                  'agent_phone_numbers',  'office_phone_numbers','social', 'country']


#define a function to detect missing values
def is_missing(value):
    if value is None:
        return True
    if isinstance(value, float) and pd.isna(value):
        return True
    if isinstance(value, str) and value.strip() == '':
        return True
    if isinstance(value, (list, dict)) and len(value) == 0:
        return True
    return False

#check missing or empty fields
missing_data = {}

for field in required_fields:
    missing_entries = df[df[field].apply(is_missing)]
    missing_data[field] = len(missing_entries)

#display results of missing counts
for field, count in missing_data.items():
    print(f"Missing '{field}': {count} entries")



Output: 
0         https://www.realliving.com/chelsea.calabrese
1       https://www.realliving.com/lizjennifer.vazquez
2          https://www.realliving.com/steven.tsukamoto
3            https://www.realliving.com/ladd.tsukamoto
4    https://www.realliving.com/kristin-tsukamoto-r...
5          https://www.realliving.com/meredith.timulty
6               https://www.realliving.com/lynn.roeder
7               https://www.realliving.com/tony.marino
8              https://www.realliving.com/jeralia.kolb
9              https://www.realliving.com/david.devore
Name: profile_url, dtype: object
Checked 12 records. Found 0 invalid profile URLs.
Missing 'title': 12 entries
Missing 'office_name': 0 entries
Missing 'address': 0 entries
Missing 'city': 0 entries
Missing 'state': 0 entries
Missing 'zipcode': 0 entries
Missing 'profile_url': 0 entries
Missing 'languages': 10 entries
Missing 'description': 2 entries
Missing 'first_name': 0 entries
Missing 'middle_name': 11 entries
Missing 'last_name': 2 entries
Missing 'website': 0 entries
Missing 'email': 0 entries
Missing 'image_url': 0 entries
Missing 'agent_phone_numbers': 0 entries
Missing 'office_phone_numbers': 1 entries
Missing 'social': 11 entries
Missing 'country': 0 entries
