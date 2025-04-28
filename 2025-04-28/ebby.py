import pandas as pd
import json
import re

#load JSON file
df = pd.read_json('ebby_2025_04_05.json',lines=True)

#print first 10 urls for viewing
print(df["profile_url"].head(10))

#display urls as text file
df["profile_url"].to_csv("profile_urls.txt", index=False, header=False)

#define  profile URL pattern
profile_url_pattern = re.compile(r'^https:\/\/www\.ebby\.com\/bio\/[a-zA-Z0-9\-]+$')

#apply regex to validate each profile URL
df['is_valid_profile_url'] = df['profile_url'].apply(lambda x: bool(profile_url_pattern.match(str(x))))

#save invalid profile URLs for review
invalid_profiles = df[~df['is_valid_profile_url']]
invalid_profiles.to_csv('invalid_profiles.csv', index=False)

#print number of records checked and records with invalid profile urls
print(f"Checked {len(df)} records. Found {len(invalid_profiles)} invalid profile URLs.")


#define fields you want to check
required_fields = ['first_name', 'last_name', 'office_name', 'title', 'description', 
                   'image_url', 'address', 'city', 'state', 'country', 'zipcode', 'office_phone_numbers',
                   'agent_phone_numbers', 'email', 'profile_url', 'website','social']


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
0               https://www.ebby.com/bio/190richardson
1                https://www.ebby.com/bio/aaronharrell
2               https://www.ebby.com/bio/aaronharrison
3                 https://www.ebby.com/bio/aaronlindig
4                  https://www.ebby.com/bio/abealarcon
5                 https://www.ebby.com/bio/acadiasmith
6                  https://www.ebby.com/bio/accounting
7                https://www.ebby.com/bio/adambouaazzi
8                     https://www.ebby.com/bio/adarosa
9    https://www.ebby.com/bio/advertisingandpublicr...
Name: profile_url, dtype: object
Checked 1501 records. Found 0 invalid profile URLs.
Missing 'first_name': 0 entries
Missing 'last_name': 61 entries
Missing 'office_name': 4 entries
Missing 'title': 189 entries
Missing 'description': 97 entries
Missing 'image_url': 320 entries
Missing 'address': 10 entries
Missing 'city': 10 entries
Missing 'state': 0 entries
Missing 'country': 0 entries
Missing 'zipcode': 11 entries
Missing 'office_phone_numbers': 1459 entries
Missing 'agent_phone_numbers': 103 entries
Missing 'email': 58 entries
Missing 'profile_url': 0 entries
Missing 'website': 1050 entries
Missing 'social': 1176 entries
