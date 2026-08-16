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
