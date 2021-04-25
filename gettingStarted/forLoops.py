list = ["Apples", "Banana", "manggo"]

for item in list:
    print(item)

print(list[:2])  # Result in array

for i in range(0, 10):  # Kasi jarak buat cetak index dari 0 - 9
    print(i)

print("")

for i in range(0, 9, 2):  # Modify to not increment by 1 but by 2
    print(i)

# Call index in 'for'
for idx, item in enumerate(list):
    print(idx, item)

# Manipulate array in specific array
listSize = len(list)
for i in range(1, listSize):
    item = list[i]
    print(item)
