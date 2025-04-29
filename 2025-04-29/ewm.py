import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('ewm_2025_05_05.json',lines=True)

#print first 10 urls for viewing
print(df["profile_url"].head(10))

#display urls as text file
df["profile_url"].to_csv("ewm_profile_urls.txt", index=False, header=False)

#define  profile URL pattern
profile_url_pattern = re.compile(r'^https:\/\/www\.ewm\.com\/agents\/\d+\/[a-zA-Z0-9\%+.-]+$')


#apply regex to validate each profile URL
df['is_valid_profile_url'] = df['profile_url'].apply(lambda x: bool(profile_url_pattern.match(str(x))))

#save invalid profile URLs for review
invalid_profiles = df[~df['is_valid_profile_url']]
invalid_profiles.to_csv('ewm_invalid_profiles.csv', index=False)

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
0       https://www.ewm.com/agents/1776696/Adam+Walder
1    https://www.ewm.com/agents/1777198/Adelaide+En...
2    https://www.ewm.com/agents/1777154/Adelina+Pan...
3    https://www.ewm.com/agents/1776798/Adolfo+J.+M...
4    https://www.ewm.com/agents/1777175/Adriana+Arango
5        https://www.ewm.com/agents/1777235/Ady+Artime
6       https://www.ewm.com/agents/1777214/Akos+Straub
7       https://www.ewm.com/agents/1776987/Alba+Biondi
8    https://www.ewm.com/agents/1777031/Albert+Laza...
9    https://www.ewm.com/agents/1792436/Alejandro+V...
Name: profile_url, dtype: object
Checked 571 records. Found 0 invalid profile URLs.
Missing 'first_name': 0 entries
Missing 'middle_name': 453 entries
Missing 'last_name': 30 entries
Missing 'office_name': 1 entries
Missing 'title': 0 entries
Missing 'description': 450 entries
Missing 'languages': 477 entries
Missing 'image_url': 155 entries
Missing 'address': 0 entries
Missing 'city': 0 entries
Missing 'state': 0 entries
Missing 'country': 0 entries
Missing 'zipcode': 0 entries
Missing 'office_phone_numbers': 0 entries
Missing 'agent_phone_numbers': 17 entries
Missing 'email': 571 entries
Missing 'website': 1 entries
Missing 'social': 355 entries
Missing 'profile_url': 0 entries
