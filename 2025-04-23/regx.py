#search for match
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
Output:YES! We have a match!

#search for price
import re
text = "The price is $45.50 and the ID is ID1234."
# Find price
price = re.search(r"\$\d+\.\d{2}", text)
print(price.group())  
Output:$45.50

# Find all uppercase letter words
words = re.findall(r"\b[A-Z]+\b", text)
print(words)  
Output:['ID']

# Replace dollar sign with "USD"
updated = re.sub(r"\$", "USD ", text)
print(updated) 
Output:The price is USD 45.50 and the ID is ID1234.


#Dates
import re
pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"
text = "Today's date is 23/04/2025, and yesterday was 22-04-2025.Tomorrow is 2025/04/24"
matches = re.findall(pattern, text)
print(matches)  
Output:['23/04/2025', '22-04-2025']

pattern = r"\b\d{4}-\d{2}-\d{2}\b"
text = "Deadline: 2025-04-23."
print(re.findall(pattern, text))  
Output:['2025-04-23']

pattern = r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b"
text = "The event is on April 23, 2025."
print(re.findall(pattern, text)) 
Output:['April 23, 2025']

#Phone number
pattern = r"\b\d{10}\b"
text = "My backup number is 9876543210."
print(re.findall(pattern, text))  
Output:['9876543210']

#Email
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
emails = [
    "user@example.com",
    "user.name+tag@example.co.uk",
    "invalid-email.com",
    "user@.com"
]

for email in emails:
    print(f"{email} is {'valid' if is_valid_email(email) else 'invalid'}")
Output:user@example.com is valid
user.name+tag@example.co.uk is valid
invalid-email.com is invalid
user@.com is invalid
​

#extracting mail address from text
import re
text = "Please contact us at support@example.com or sales@example.co.uk for more information."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)
print(emails)
Output: ['support@example.com', 'sales@example.co.uk']



#validate name
import re
def is_valid_name(name):
    pattern = r"^[A-Za-z]+([ -][A-Za-z]+)*$"
    return re.fullmatch(pattern, name) is not None
print(is_valid_name("John Doe"))        # True
print(is_valid_name("Anne-Marie"))  # True
print(is_valid_name("1234"))            # False
Output: True
True
False


#search
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
Output:<re.Match object; span=(5, 7), match='ai'>


#match.span()
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
Output:(12, 17)


#match.string()
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
Output:The rain in Spain


#match.group()
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
Output:Spain
