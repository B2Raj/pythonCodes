# Write a program to find the factorial of given no.

# using for loop
print("Factorial using for loop--->")
n=int(input("Enter a no.: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Fact of",n,"is:",fact)

# using while loop
print("Factorial using while loop-->")
fact=1
count=1
while count<=n:
    fact*=count
    count+=1
print("Factorial of",n,"is:",fact)