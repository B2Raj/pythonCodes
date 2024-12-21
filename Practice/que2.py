# Write a program to convert USD to INR

def convertCurrency(a):
    inr=a*83.2
    print(a,"USD equals to",inr,"INR")
n=int(input("Enter amount in USD:"))
convertCurrency(n)