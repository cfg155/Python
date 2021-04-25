class Person:
    def getName(self):
        print('louis')

    def getAge(self):
        print(21)


p = Person()

p.getName()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print('Your name is ' + self.name)

    def getAge(self):
        print('Your Age is ' + self.age)


p = Person('Louis', 21)

p.getName()
