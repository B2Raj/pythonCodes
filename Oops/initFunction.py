# init Fucntion(Constructor):- All classes have a funciton called __init__(), which is always executed when the object is being initiated. 
# Note:- init function always takes a parameter.
# syntax:- def __init__():

class Cycle:
    name="Hero"
    def __init__(self):
        print("Hii, this is B2")
c1=Cycle()
print(c1.name)

class Cycle:
    def __init__(self):
        print("Hii, this is B2")
    name="Hero"
c1=Cycle()
print(c1.name)

# In Both class, init functions executed first.