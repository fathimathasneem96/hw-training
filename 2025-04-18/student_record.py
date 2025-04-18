# Create a dictionary to store student information
students= {
 'student_1':{
'Name':'Aleena John',
'Age':14,
'Marks':[89.0,93.7,87.5]  },
'student_2':{
'Name':'James',
'Age':15,
'Marks':[63.5,44.8,54.2 ]},
'student_3':{
'Name':'Haya',
'Age':14,
'Marks':[84.8,91.5,79.6]  },
'student_4':{
'Name':'Akhil',
'Age':16,
'Marks':[59.8,86.9,79.5]  }
}


# Subject names in a tuple
subjects = ('English','Maths','science')

# Function to calculate total and average marks for each student and determine pass/fail status
for student, details in students.items():
    name = details['Name']
    age = details['Age']
    marks = details['Marks']
    
    # Printing the data types of each value
    print(f"{name}'s Data Types:")
    print(f"Name type: {type(name)}")
    print(f"Age type: {type(age)}")
    print(f"Marks type: {type(marks)}")
    
    # Calculate total and average marks
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    
    # Determine if the student passed
    if average_marks>=40:
    	print("Passed")
    else:
    	print("Failed")
    
    # Print individual marks
    print(f"\nIndividual Marks for {name}:")
    for subject, mark in zip(subjects, marks):
        print(f"{subject}: {mark}")
    
    # Convert marks list to a set and print
    marks_set = set(marks)
    print(f"\nMarks Set (unique): {marks_set}")
    
    # Print subject names
    print(f"\nSubjects: {subjects}")
    
    # Print remarks variable (None)
    remarks = None
    print(f"\nRemarks: {remarks}, Type: {type(remarks)}")

    # Determine if the student passed
    is_passed = average_marks >= 40

    # Print pass/fail status
    print(f"\nIs {name} Passed? {'Yes' if is_passed else 'No'}, Type: {type(is_passed)}")
  

    print("-" * 30)

for student, details in students.items():
    # Print student report
    print(f"\n{student} Report:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Pass/Fail: {'Passed' if is_passed else 'Failed'}") 
    print()
