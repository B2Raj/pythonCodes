# Method 1st


name=input("Enter name:")
_Name=("B2") if name=="Bittu" else "No"
print(_Name)



# Method 2nd


name2=input("Enter name: ")
print("B2") if name2=="Bittu" or name2=="bittu" else print("Invalid name")



# clever ternary operator


age=int(input("Enter Your Age: "))
vote=("Yes","No")[age<=18]
print(vote)


# clever ternary operator 2nd example


salary=int(input("Enter your Salary: "))
sal=("Good","Bad")[salary<100000]
print(sal)
