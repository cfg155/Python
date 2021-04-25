# abs return absolute number without any minus
print(abs(-20))

# bool => Accept all numbers except 0 and None
print(bool(0))  # Result false
print(bool(None))  # Result False
print(bool(1))  # Result True

# dir => check what syntax i can use for certain data type
print(dir("hello"))

# To check the meaning of the syntax u just found in dir just use help
print(help("hello".upper))

# eval => convert strings into python code
x = 'print("Hiii")'
eval(x)

# Convert data type
x = 1

print(str(x))  # convert into str
print(float(x))  # convert into float
print(int(x))  # convert into int
