# General Way
students = ["Jake", 20, "Albert", 15]
print(students)

# Object
students = {"Jake": 20, "Albert": 15}
print(students)
print(students["Jake"])  # find the attribute in Object

# Edit attribute
students["Jake"] = 30
print(students)

# Remove Attribute
del students["Albert"]
print(students)

print(len(students))  # Get size of object
