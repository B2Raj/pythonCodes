

"""Tuples are built-in data type that are used to store data enclosed by Small Brackets
Also tuple object cannot updates by assigning """

tup=(3,2,2,3,45)
print(tup)
print(type(tup))        # Type of tuple
print(tup[3])       # We can access the elements using indexes
print(tup[2])
tup2=()      # We can also print empty tuple
print(tup2)
print(type(tup2))
print(tup2)




""" IfHere, we can also take single digit only 3, but when we take like that then Python will consider
it an integer value. for example:- """
tup4=(3)
print(tup4)
print(type(tup4))
""" ThereFore, we use a single comma after an element so that it will consider it as Tuple """
tup3=(3,)
print(type(tup3))
print(tup3)


# WE can also Slice in Tuples

tup5=(4,2,2,3,5,2)
print(tup5[2])
print(tup5[5])
print(tup5[-2])
print(tup5[2:5])
print(tup5[0:-2])


# We can also find the indeces of tuple's data

tuple=(3,2,5,2,1,5)
print(tuple.index(3))
print(tuple.index(5))
# print(tuple.index(4)) ,, This line gives us Error because 4 is not in the Tuple







#   We can also count the occurence of elements in Tuple

tuple1=(4,2,2,2,45,2,1,4,4,4,4,4)
print(tuple1.count(4))
print(tuple1.count(25))
print(tuple1.count(45))







