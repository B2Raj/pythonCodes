class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Students("Bittu",18)
print(s1.name)
print(s1.age)
del (s1)
del(s1.age)