# Tuples is permanent state value, meaning u can't update or change the value
tup = ("Apples", "Banana", "Orange")
print(tup[0])
print(tup[0:2])

# Combine Tuples
tup2 = (15, 21)
tup3 = tup + tup2
print(tup3)

print(len(tup))  # Get tuple size

tup = ("Hi")
print(tup*4)
