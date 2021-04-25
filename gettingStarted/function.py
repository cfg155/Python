def helloWorld():  # Function without Parameter
    print("Hello world")


helloWorld()


def greeting(name):  # Function with parameter
    print("Hi! " + name)


greeting("Louis")


def sumNumb(num1, num2):  # Function with multiple parameter
    print(num1 + num2)


sumNumb(1, 2)


def multiplicity(num1, num2):  # Function with return statement
    return num1*num2


result = multiplicity(2, 2)
print(result)
