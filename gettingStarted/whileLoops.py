x = 0
while x < 5:
    print(x)
    x = x+1

x = 0
while x < 5:
    print(x)
    if(x == 3):
        break  # Stop Looping
    x = x + 1

print("")

x = 0
while x < 5:
    x = x + 1
    if(x == 3):
        continue  # Skip pada idx tertentu
    print(x)
