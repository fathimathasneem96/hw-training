import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('coldwellbanker_us_2025_05_05.json',lines=True)

#print first 10 urls for viewing
print(df["profile_url"].head(10))

#display urls as text file
df["profile_url"].to_csv("coldwell_profile_urls.txt", index=False, header=False)

#define  profile URL pattern
profile_url_pattern = re.compile(r'^https:\/\/www\.coldwellbanker\.com\/[/a-zA-Z0-9\-._]+$')

#apply regex to validate each profile URL
df['is_valid_profile_url'] = df['profile_url'].apply(lambda x: bool(profile_url_pattern.match(str(x))))

#save invalid profile URLs for review
invalid_profiles = df[~df['is_valid_profile_url']]
invalid_profiles.to_csv('coldwell_invalid_profiles.csv', index=False)

#print number of records checked and records with invalid profile urls
print(f"Checked {len(df)} records. Found {len(invalid_profiles)} invalid profile URLs.")


#define fields want to check
required_fields = ['first_name', 'middle_name', 'last_name', 'office_name', 'title', 'description', 
                   'languages', 'image_url', 'address', 'city', 'state', 'country', 'zipcode', 
                   'office_phone_numbers', 'agent_phone_numbers',  'email', 'website','social', 'profile_url', ]


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
0    https://www.coldwellbanker.com/il/schaumburg/a...
1    https://www.coldwellbanker.com/il/long-grove/a...
2    https://www.coldwellbanker.com/il/long-grove/a...
3    https://www.coldwellbanker.com/il/chicago/agen...
4    https://www.coldwellbanker.com/il/schaumburg/a...
5    https://www.coldwellbanker.com/il/highland-par...
6    https://www.coldwellbanker.com/il/long-grove/a...
7    https://www.coldwellbanker.com/il/chicago/agen...
8    https://www.coldwellbanker.com/il/long-grove/a...
9    https://www.coldwellbanker.com/il/glencoe/agen...
Name: profile_url, dtype: object
Checked 74144 records. Found 0 invalid profile URLs.
Missing 'first_name': 0 entries
Missing 'middle_name': 71168 entries
Missing 'last_name': 312 entries
Missing 'office_name': 0 entries
Missing 'title': 0 entries
Missing 'description': 25418 entries
Missing 'languages': 10919 entries
Missing 'image_url': 5231 entries
Missing 'address': 0 entries
Missing 'city': 0 entries
Missing 'state': 0 entries
Missing 'country': 0 entries
Missing 'zipcode': 0 entries
Missing 'office_phone_numbers': 1 entries
Missing 'agent_phone_numbers': 18229 entries
Missing 'email': 8393 entries
Missing 'website': 19495 entries
Missing 'social': 43976 entries
Missing 'profile_url': 0 entries
