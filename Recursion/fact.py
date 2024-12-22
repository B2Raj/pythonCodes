# Calculalte factorial of a number using recursion

def factorial(a):
    if(a==0):
        return 1
    else:
        return a*factorial(a-1)
n=int(input("Enter a no.:"))
x=factorial(n)
print("Factorial of",n,"is:",x)