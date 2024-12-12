# Write a program to check if a number entered by user is odd or even

n=int(input("Enter a number: "))
if(n%2==0):
    print("The no. is even")
else:
    print("The no. is odd")


# Write a program to find the greatest of 3 numbers entered by user
num1=int(input("Enter 1st no.:"))
num2=int(input("Enter 2nd no.:"))
num3=int(input("Enter 3rd no.:"))
if(num1>num2 and num1>num3):
    print(num1, " is Greatest")
elif(num2>num3):
    print(num2, " is Greatest")
else:
    print(num3, " is Greatest")


# Write a program to check wether the no. is multiple of 7 or not


n=int(input("Enter a number: "))
if(n%7==0):
    print("The no. is multiple of ",n)
else:
    print("The no. is not multiple of ",n)
    
