

#   (Que.1) Write a program to ask the user to enter names of their 3 favourite movies and store them in a list.

print("---->Write down your favourite movies:")
movie1=input("Enter 1st movie:")
movie2=input("Enter 2nd movie:")
movie3=input("Enter 3rd movie:")
listOfMovies=[movie1,movie2,movie3]
print("List of Your Favourite is: ",listOfMovies)


  # Another Way to store in the list is
## In this method, we used  function to add in the list
print("----> Write down your favourite movies: ")
movies=[]
mov1=input("Enter 1st movie: ")
mov2=input("Enter 2nd movie: ")
mov3=input("Enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)


    # Third method to store in the list is

print("----> Write down your favourite movies: ")

movie_=[]
movie_.append(input("Enter 1st movie: "))
movie_.append(input("Enter 2nd movie: "))
movie_.append(input("Ente3 3rd movie: "))
print(movie_)



"""  (Que2)  Write a program to enter names of their 3 favourite movies and store them in a list.
    So, to identify it that it is pallindrone or not, first we will creat a list for which we will check the
    condition.Then, we will create a copy of that list and then we will reverse that copied list. After
    reversing the copied list, if the copied list will be equal to the origional list then it will
    pallindrone else not a pallindrone """
    # Also we can check the pallindrone condition for string

list=[4,5,6,6,5,4]
print(list)
copyList=list.copy()    # name.copy() function is used to create a copy of list
copyList.reverse()      #  This function will reverse the list
print(copyList)
list2=['b','c','e','c','d']
""" In this code of pallindrone, both the list should be Pallindrone."""
print(list2)                # Note:- We can also code for 1 list
copyList2=list2.copy()
copyList2.reverse()
print(list2)

if(list==copyList and list2==copyList2):
    print("Pallindrone")
else:
    print("Not a Pallindrone")




""" (Que.3)  Write a programe to count the number of students with the "A" grade in the given Tuple,aslo sort in
ascending order. """
        # for this, we will use count function

grade=('A','C','D','A','C','A','B','B')
print(grade)
print("Total occurence of 'A' Grade is: ",grade.count("A"))
print("Total occurence of 'c' Grade is: ",grade.count("C"))
  # for sorting those grades in ascending order, we can create another list using same data then 
gradeForSort=['A','C','D','A','C','A','B','B']
gradeForSort.sort()
print("Grades in Sorted order will be: ",gradeForSort)
