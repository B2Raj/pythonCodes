# Write a recursive function to calculate the sum of first n natural numbers.

def calSum(a):
    if(a==0):
        return 0
    else:
        return a+calSum(a-1)
n=int(input("Enter a no.:"))
sum=calSum(n)
print("Sum is:",sum)