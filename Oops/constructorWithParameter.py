# the constructor/init function which has only self parameter called defaultl constructor. while the constructor which has some parameters called parameterised constructor.

class Student:
    def __init__(self,name):
         self.name=name
s1=Student("Bittu")
print(s1.name)
s2=Student("Anand")
print(s2.name)
s3=Student("Vicky")
print(s3.name)