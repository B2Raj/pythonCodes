# traffic lights


light=input("Enter color of Lights: ")
print(light)
if(light=="red" or light=="Red"):
    print("Stop")
elif(light=="yellow" or light=="Yellow"):
    print("Look")
elif(light=="green" or light=="Green"):
    print("Go")
else:
    print("Light is Broken")


# voting

age=int(input("Enter Your Age: "))
print(age)
if(age>=18 and age<120):
    print("Person can Vote: ")
elif(age<18):
    print("Person cannot Vote: ")
elif(age>=120):
    print("Invalid age")


# Grade of students

marks=int(input("Enter Your Marks: "))
print("Your Marks is: ",marks)
if(marks>=95 and marks<=100):
    print("A+ Grade")
elif(marks>=80 and marks<95):
    print("A Grade")
elif(marks>=70 and marks<100):
    print("B Grade")
elif(marks>=60 and marks<100):
    print("C Grade")
elif(marks>=40 and marks<=100):
     print("D Grade")
elif(marks>100):
    print("Invalid Marks")
else:
    print("Fail")



