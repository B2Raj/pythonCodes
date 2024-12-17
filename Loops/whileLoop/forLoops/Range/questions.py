# odd no
print("-->Example 1")
print("oddNo.")
for i in range(1,10,2):
    print(i)

print("-->Example 2")
print("evenNo.")
for i in range(0,10,2):
    print(i)

print("-->Example 3")
print("oddNo using if/else in for loops.")
# odd No using if/else
for i in range(10):
    if(i%2!=0):
        print(i)

print("-->Example 4")
# evenNo using if/else
print("EvenNo using if/else in for loops.")
for i in range(10):
    if(i%2==0):
        print(i)
        
print("-->Example 5")
# 1 to 100
for i in range(1,101):
    print(i)
    
print("-->Example 6")
# 1 to 100 from backword
for i in range(100,0,-1):
    print(i)
    
print("-->Example 7")
# multiple of n
n=int(input("Enter a no.: "))
for i in range(1,11):
    print(i*n)
    