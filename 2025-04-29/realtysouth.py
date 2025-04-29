import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('realtysouth_2025_05_05.json',lines=True)

#print first 10 urls for viewing
print(df["profile_url"].head(10))

#display urls as text file
df["profile_url"].to_csv("realtysouth_profile_urls.txt", index=False, header=False)

#define  profile URL pattern
profile_url_pattern = re.compile(r'^https:\/\/www\.realtysouth\.com\/(bio|roster)\/[a-zA-Z0-9/-]+$')


#apply regex to validate each profile URL
df['is_valid_profile_url'] = df['profile_url'].apply(lambda x: bool(profile_url_pattern.match(str(x))))

#save invalid profile URLs for review
invalid_profiles = df[~df['is_valid_profile_url']]
invalid_profiles.to_csv('realtysouth_invalid_profiles.csv', index=False)

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
0    https://www.realtysouth.com/bio/carrieeasterling
1        https://www.realtysouth.com/bio/carriegitter
2     https://www.realtysouth.com/bio/carriehillsmith
3         https://www.realtysouth.com/bio/cassiesmith
4       https://www.realtysouth.com/bio/catherinebode
5     https://www.realtysouth.com/bio/catherinepewitt
6       https://www.realtysouth.com/bio/cathiegroover
7     https://www.realtysouth.com/bio/ceceliathompson
8          https://www.realtysouth.com/bio/cecilclark
9       https://www.realtysouth.com/bio/celestenabors
Name: profile_url, dtype: object
Checked 706 records. Found 0 invalid profile URLs.
Missing 'first_name': 0 entries
Missing 'middle_name': 686 entries
Missing 'last_name': 1 entries
Missing 'office_name': 0 entries
Missing 'title': 0 entries
Missing 'description': 48 entries
Missing 'languages': 688 entries
Missing 'image_url': 19 entries
Missing 'address': 0 entries
Missing 'city': 0 entries
Missing 'state': 0 entries
Missing 'country': 0 entries
Missing 'zipcode': 0 entries
Missing 'office_phone_numbers': 0 entries
Missing 'agent_phone_numbers': 0 entries
Missing 'email': 706 entries
Missing 'website': 24 entries
Missing 'social': 458 entries
Missing 'profile_url': 0 entries
