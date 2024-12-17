# range means the functions that returns a sequence of numbers, starting from 0(by default), and stops before a specified numbers.
# - condition-->range(start,stop,step)
# If we initialist range with only a number then it will By default its starting index will be initialised by 0 as ex1 and also step no is by default increament by 1.

# example 1
print("Example 1")
print(range(3))     # range(0,3)

# example 2
print("Example 2")
x=range(2,4)
print(x)    # range(2,4)

# example 3
print("Example 3")
for i in range(2,6):
    print(i)    # 0,1,2,3

# example 4
print("Example 4")
for i in range(1,10,2):
    print(i)    # 1,3,5,6,7,9
''' 1 is initial point, 10 is final point and 2 is increament no. or step no. '''

# example 5
# we can also print sequence by elements from the range
print("Example 5")
seq=range(10)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
print(seq[5])
print(seq[6]) # expected output:- 0,1,2,3,4,5,6

# example 6
print("Example 6")
seq2=range(3,15)
print(seq2[0])
print(seq2[1])
print(seq2[2])
print(seq2[3])
print(seq2[4])
print(seq2[5])
print(seq2[6])
print(seq2[7])    # expected output:- 3,4,5,6,7,8,9,10

# example 7
print("Example 7")
seq3=range(2,15,2)
print(seq3[0])
print(seq3[1])
print(seq3[2])
print(seq3[3])
print(seq3[4])
print(seq3[5])
print(seq3[6])  # expected output:- 2,4,6,8,10,12,14