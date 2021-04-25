class Parent:
    def __init__(self):
        print("This is parent Class")

    def parentFunc(self):
        print("This is parent func")

    def test(self):
        print("This is test parent")


class Child(Parent):
    def __init__(self):
        print("This is Child Class")

    def childFunc(self):
        print("This is Child Func")

    def test(self):
        print("this is Test Child")


p = Parent()  # Create Parent Object

c = Child()  # Create Child Object
c.parentFunc()  # Calling parent function through child

c.test()  # Result is "this is Test Child" it overrides the function from parents
