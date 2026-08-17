# class Animal:
#     def eat(self):
#         print("Animal is eating")

#     def sleep(self):
#         print("Animal is sleeping")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")


# dog = Dog()

# dog.eat()
# dog.sleep()
# dog.bark()






class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Bruno", "Labrador")

print(dog.name)
print(dog.breed)        




class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()




class Animal:
    def __init__(self, name):
        self.name = name

class Child(Animal):
    pass

dog = Child("bruno")
print(dog.name)






class Fruit:

    def __init__(self, name):
        self.name = name

    def kiwi(self, colour):
        self.colour = colour
        print("Fruit:", self.name, colour)

class Veg(Fruit):

    def __init__(self, name):
        self.name = name

    # OVERRIDING
    def kiwi(self, colour):
        print("Veg kiwi")
        print( colour)

    def tomato(self):
        print("Tomato:", self.name)

    def potato(self, dish):
        self.dish = dish
        print("Potato:", self.dish)


obj = Veg("Vedant")

obj.kiwi("green")
obj.potato("fries")
obj.tomato()




class Fruit:

    def __init__(self, name):
        self.name = name

    def kiwi(self):
        print("Fruit:", self.name)


class Veg(Fruit):

    def __init__(self, name,colour):
        self.colour = colour
        # self.name = name
        super().__init__(name)
        print(self.colour)
        

    def tomato(self):
        print("Tomato:", self.name)


obj = Veg("Vedant","blue")

obj.tomato()
obj.kiwi()




class Car:
    def start(self):
        print("Car is starting")


class ElectricCar(Car):
    def start(self):
        super().start()
        print("Electric motor is starting")


car = ElectricCar()

car.start()








