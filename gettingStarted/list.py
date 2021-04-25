list = ["Apple", "Orange", "Banana"]
print(list[0])  # Get the index 0 of array
print(list[:2])  # Get index from 0-1
list.append("Melon")  # Add new item to array
print(list)

list[0] = "Pier"  # Edit item in index 0
print(list)

del list[0]  # Remove the index 0 in array
print(list)

print(len(list))  # length or size of the array

# Combine arrays
newList = ["Pizza", "Bread"]
print(list + newList)

# Int array
intArr = [21, 1, 4, 2, 14]
print(max(intArr))  # Max number in array
print(min(intArr))  # Min Number in array
