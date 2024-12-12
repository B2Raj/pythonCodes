# area of square


side=int(input("Enter side of Square: "))
area=side*side
print("Area of Square is: ",area)

# perimeter and area of rectangle

length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
area=length*breadth
perimeter=2*(length+breadth)
print("Area of Rectangle is: ",area)
print("Perimeter of Rectangle is: ",perimeter)


# Average of two number

a=int (input("Enter 1st(a) no.: "))
b=int (input("Enter 2nd(b) no.: "))
print("Average of a and b is: ", (a+b)/2)


# check wether which one is greater between two input no.


a=int(input("Enter 1st no.: "))
b=int(input("Enter 2nd no.: "))
if(a>b):
    print("1st no. is Greater: ")
elif(a==b):
        print("Both numbers are equal: ")
else:
    print("2nd no. is Greater: ")
