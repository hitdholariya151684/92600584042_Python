student = {
    "name": "heet",
    "age": 22,
    "course": "Python"
}

# Access value
print(student["name"])

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Add value
student["city"] = "Rajkot"

# Iteration
for key, value in student.items():
    print(key, ":", value)
