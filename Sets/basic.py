""" Set is the collection of the unordered items. Each element in the set must be unique and immutable. """

# List and Dictionaries cannot be stored in Sets because these are mutable bur tuples can be store in Sets

collectionOfNumbers={1,2,4,3,"Bittu","Raj",4,2,6}
print(collectionOfNumbers)
print(type(collectionOfNumbers))
print(len(collectionOfNumbers))


# We can also create a empty set

emptyset={}     # This will create a empty dictionary
print(type(emptyset))


# So to create an empty set

emptySet=set()
print(emptyset)
print(type(emptySet))


        # Methoss or function in sets

# set.add(elements)  add an element
# set.remove(element)  remove an element
# set.clear()   empties the set
# set.pop()   remove a random value
# set.union(set2)   combines both set value and return new, in one shot, union avoid repeating 
# set.intersection(set2)  combines common value and returns new, in one shot, intersection given common elements

        # Note:- Sets are mutable but set's elements are immutable

set=set()        # empty set
set.add(32)
set.add(33)
set.add(44)
set.add(42)
set.add(32)  # This elements will ignored by set because this is repeating elements
print(set)
set.remove(33)
print(set)
set.add(55)
print(set)
set.pop()
print(set)
set.add("Bittu")
print(set)
set.add(("B2","Raj"))  # tuples
print(set)
set.clear()
print(set)

# for union and intersection

set1={3,1,4,2,8}
set2={4,1,6,7,9}
print(set1.union(set2))
print(set1.intersection(set2))


# Questions

# Que(1). Store followint word meaning in a python dictionary:

table={"cats":"a small animals","Table":{"A piece of furniture","list of facts and figures"}}
print(table)
print(len(table))


"""  Que(2). You are given a list of subjects for students. Assume one classroom is required for 1 subject. How
many classrooms are needed by all subjects.
            These are the subjects accordint to students means for python there are 3 students and so on...
   ["python","java","C++","python","javascript","java","python","java","C++","C"]"""
"""  Form table, there will be 5 class needed by students. for total no, of students we can store all the data
 in the set and then we can get length of data that will be the no. of classrooms. """

subject={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(subject)
print("No. of classRooms for students are: ",len(subject))


""" Que(3). WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty
dictionary and add one by one. Use subject name as key and marks as value. """

sub1=int(input("Enter phy marks: "))
sub2=int(input("Enter maths marks: "))
sub3=int(input("Enter computer marks: "))
marks={}    # dictionary named marks
marks.update({"Physics":sub1})
marks.update({"Maths":sub2})
marks.update({"Computer":sub3})
print(marks)


""" Que(4). Figure out a way to store 9 and 9.0 as separate values in the set.(you can take help of built-in
    data types.  """

# In set, no like 4 and 4.0 are considered as same values so two make it different, the first method is

ss={9,"9.0"}
print(ss)

# 2nd method is to make it different is by using built-in data types

newSet={("float",9.0),("int",9)}
print(newSet)
print(len(newSet))
print(type(newSet))































