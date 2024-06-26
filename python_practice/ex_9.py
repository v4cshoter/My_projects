class First:

    def get_name(self):
        return self.__class__.__name__

    @classmethod
    def get_type(cls):
        return cls.__name__


class Second:
    def get_name(self):
        return "First"


class Third:

    def get_programming_language(self):
        return "Python"


class Fourth(First, Second, Third):
    def get_programming_language(self):
        return "c++"


# a = First()
# b = Second()
# c = Third()
# d = Fourth()
# print(a.get_name())
# print(b.get_name())
# print(c.get_programming_language())
# print(d.get_name())
# print(d.get_programming_language())
# print(d.get_type())


class Cat:
    def say(self):
        print("Мяу")


class Dog:
    def say(self):
        print("Гав")


class CatDog(Cat):
    def say(self):
        super().say()
        print("Гав")


c = Cat()
c.say()
d = Dog()
d.say()
cd = CatDog()
cd.say()
