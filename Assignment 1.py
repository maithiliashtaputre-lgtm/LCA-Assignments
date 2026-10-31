#Q1

student_data = {
    "101": {
        "Name": "Rahul",
        "Roll Number": "101",
        "Branch": "CSE",
        "Subjects": ["Python", "Physics", "Chemistry", "Math"],
        "Marks": (98, 95, 92, 97)
    }
}


student_data["102"] = {
    "Name": "Priya",
    "Roll Number": "102",
    "Branch": "IT",
    "Subjects": ["Python", "Physics", "Chemistry", "Math"],
    "Marks": (90, 94, 89, 96)
}

student_data["101"].update({"Branch": "AI"})

del student_data["102"]

print("Final Student Records:")
print(student_data)
