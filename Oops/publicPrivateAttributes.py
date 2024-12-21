# To make something private, we can use double underscore before that attributes 
class Account:
    def __init__(self,accountNo,accountPass):
        self.accountNo=accountNo    # public attributee
        self.__accountPass=accountPass    # private attribute
    def resetPass(self):
        print(self.__accountPass)
a1=Account(1234567,"BittuRaj")
print(a1.accountNo)
print(a1.__accountPass)