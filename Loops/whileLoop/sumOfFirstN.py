# Write a program to print the sum of first n natural no.
print("Using for loop---->")
n=int(input("Enter a no.: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of first",n,"is: ",sum)

#same question using While loop
print("Using while loop---->")
sum=0
count=1
while count<=n:
    sum+=count
    count+=1
print("Sum is:",sum)