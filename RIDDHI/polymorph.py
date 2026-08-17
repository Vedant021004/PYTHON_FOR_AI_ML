# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()



class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")


class Cat(Animal):
    def sound(self):
        super().sound()
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()



class Car:
    def start(self):
        print("Car started")


class Computer:
    def start(self):
        print("Computer started")


def start_device(device):
    device.start()


# start_device(Car())   # car().start
# start_device(Computer())

Car().start()
Computer().start()


print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])