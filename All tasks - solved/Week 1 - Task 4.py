students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# 1) Get Alice's AI301 grade
alice_data = students.get("S001", {})
alice_courses = alice_data.get("courses", {})
ai301_info = alice_courses.get("AI301", {})
alice_grade = ai301_info.get("grade",{})

print(f"1) Alice AI301 Grade: {alice_grade}")


# 2) Calculate Bob's GPA
bob_courses = students["S002"]["courses"]
bob_gpa = sum(c["grade"] * c["credits"] for c in bob_courses.values()) / sum(c["credits"] for c in bob_courses.values())
print(f"2) Bob GPA: {bob_gpa:.2f}")



# 3) Find all students in CS101
cs101_list = [s["name"] for s in students.values() if "CS101" in s["courses"]]
print(f"3) Students in CS101: {cs101_list}")


# 4) Get average grade across all courses
all_grades = [c["grade"] for s in students.values() for c in s["courses"].values()]
average = sum(all_grades) / len(all_grades)
print(f"4) Global Average: {average:.2f}")



# 5) Find student with highest GPA
top_student = max(students.values(), key=lambda s: sum(c["grade"]*c["credits"] for c in s["courses"].values()) / sum(c["credits"] for c in s["courses"].values()))
print(f"Top Student: {top_student['name']}")
