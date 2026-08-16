# overloding------------------------------------
 


class Calculator:

    def add(self, a=0, b=0, c=0):
        print(a + b + c)


calc = Calculator()

calc.add(10)
calc.add(10, 20)
calc.add(10, 20, 30)



# encapsulation -------------------------------

class Car:

    def __init__(self, speed):
        self.__speed = speed

    def show_speed(self):
        print("the hidden variable is :",self.__speed)


car = Car(100)

car.show_speed()


# second problem ------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.amount = amount

    def show_balance(self):
        print(self.__balance + self.amount)


account = BankAccount(1000)

account.deposit(500)
account.show_balance()


# third question -------------------------------

class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):

        return self.marks


student = Student()

student.set_marks(85)

print(student.get_marks())



# access hte private variables

class Car:

    def __init__(self):
        self.__speed = 120
        print(self.__speed)

    def getter(self):
        return self.__speed

car = Car()

print(car.getter())


# bankaccount -----------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        self.amount = amount
        if amount > 0:
            self.__balance += amount


    def withdraw(self, amount):

        if amount > 0 and amount < self.__balance:
            self.__balance -= amount

        

    def get_balance(self):

        return self.__balance


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)

print(account.get_balance())



# Student Exampple------------------

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

    def get_marks(self):
        return self.__marks

obj = Student(23)    
print(obj.set_marks(39))
print(obj.get_marks())



# Employee -----------------------

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

    def get_salary(self):
        return self.__salary

    