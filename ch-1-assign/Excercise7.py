student = {
    "name": "heet",
    "age": 20,
    "course": "advance Python"
}

# Access value
print(student["name"])

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Add value
student["city"] = "rajkot"

# Iteration
for key, value in student.items():
    print(key, ":", value)
