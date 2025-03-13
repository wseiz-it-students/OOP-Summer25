# students.py

# List of student dictionaries
students = [
    {
        "first_name": "adil",
        "last_name": "efe",
        "index_number": "35486",
        "nationality": "American",
        "starting_date": "2024-03-13",
        "courses": ["Mathematics", "Physics", "Computer Science"]
    },
    {
        "first_name": "jale",
        "last_name": "Smith",
        "index_number": "153657",
        "nationality": "British",
        "starting_date": "2024-03-13",
        "courses": ["Biology", "Chemistry", "English"]
    },
    {
        "first_name": "Ali",
        "last_name": "Khan",
        "index_number": "S11223",
        "nationality": "Pakistani",
        "starting_date": "2024-03-13",
        "courses": ["History", "Geography", "Economics"]
    }
]

for student in students:
    print(f"Student: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")
