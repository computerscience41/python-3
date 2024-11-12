#  12 Dictionary operations

students = {
    "Alice": 85,
    "Bob" : 90,
    "Charlic" : 78
}

print("student names:", students.keys())

students.pop("Charlic")
print("Updated dictionary:", students)