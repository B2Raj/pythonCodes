# Write a recursive function to print all elements in a list.

def printList(list,idx):
    if(idx==len(list)):
        return
    else:
        print(list[idx],end=" ")
    printList(list,idx+1)
list=[1,2,3,4,45,6,7,8]
printList(list,0)