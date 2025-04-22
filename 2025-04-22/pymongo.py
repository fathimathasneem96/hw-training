# PyMongo Advanced Examples
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
collection = db["employee"]

# 1. Insert One Document
collection.insert_one({
    "empId": 101,
    "name": "Ravi",
    "department": "IT",
    "salary": 75000,
    "isActive": True
})

# 2. Insert Many Documents
collection.insert_many([
    {"empId": 102, "name": "Alice", "department": "Sales", "salary": 50000, "isActive": True},
    {"empId": 103, "name": "John", "department": "HR", "salary": 80000, "isActive": True},
    {"empId": 104, "name": "Aysha", "department": "IT", "salary": 65000, "isActive": False}
])

# 3. Find All Documents
print("All Employees:")
for emp in collection.find():
    print(emp)

# 4. Find with Filter
print("\nEmployees in HR:")
for emp in collection.find({"department": "HR"}):
    print(emp)

# 5. Update One
collection.update_one(
    {"empId": 102},
    {"$set": {"salary": 55000}}
)

# 6. Update Many
collection.update_many(
    {"department": "Sales"},
    {"$inc": {"salary": 10000}}
)

# 7. Delete One
collection.delete_one({"empId": 103})

# 8. Delete Many
collection.delete_many({"isActive": False})

# 9. Aggregation Pipeline
pipeline = [
    {"$group": {
        "_id": "$department",
        "avgSalary": {"$avg": "$salary"},
        "maxSalary": {"$max": "$salary"},
        "minSalary": {"$min": "$salary"}
    }}
]
print("\nDepartment-wise Salary Stats:")
for result in collection.aggregate(pipeline):
    print(result)

# 10. Query with $or and $and
query = {
    "$and": [
        {"isActive": True},
        {"$or": [
            {"department": "HR"},
            {"department": "IT"}
        ]}
    ]
}
print("\nActive employees in HR or IT:")
for emp in collection.find(query):
    print(emp)

# 11. Add Timestamp Field
collection.update_many({}, {"$set": {"joinedDate": datetime.utcnow()}})
print("\nAdded 'joinedDate' to all documents")
