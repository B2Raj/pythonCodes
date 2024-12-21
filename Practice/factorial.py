# Write a program to calculate factorial of a no.

def fact(n):
    fact=1
    count=1
    while count<=n:
        fact*=count
        count+=1
    print(fact)
a=int(input("Enter a no.:"))
fact(a)