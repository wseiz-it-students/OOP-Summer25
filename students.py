students = [
    {
        "first_name": "adil",
        "last_name": "efe",
        "index_number": "35486",
        "nationality": "American",
        "starting_date": "2024-03-13",
        "courses": ["Mathematics", "Physics", "Computer Science"],
    },
    {
        "first_name": "jale",
        "last_name": "Smith",
        "index_number": "153657",
        "nationality": "British",
        "starting_date": "2024-03-13",
        "courses": ["Biology", "Chemistry", "English"],
    },
    {
        "first_name": "Ali",
        "last_name": "Khan",
        "index_number": "S11223",
        "nationality": "Pakistani",
        "starting_date": "2024-03-13",
        "courses": ["History", "Geography", "Economics"],
    },
]


def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    index_number = input("Enter index number: ")
    nationality = input("Enter nationality: ")
    starting_date = input("Enter starting date (YYYY-MM-DD): ")
    courses = input("Enter courses (comma-separated): ").split(", ")

    students.append(
        {
            "first_name": first_name,
            "last_name": last_name,
            "index_number": index_number,
            "nationality": nationality,
            "starting_date": starting_date,
            "courses": courses,
        }
    )
    print("Student added successfully!\n")


def display_students():
    for s in students:
        print(
            f"{s['first_name']} {s['last_name']} - {s['index_number']} - {s['nationality']} - {s['starting_date']} - Courses: {', '.join(s['courses'])}"
        )


add_student() 
display_students() 


