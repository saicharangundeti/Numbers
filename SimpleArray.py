from array import *
arr=array('i',[])
val=int(input("Enter the size of array:"))
for i in range(val):
    x=int(input("enter the element:"))
    arr.append(x)
print(arr)
print((max(arr)+ min(arr)))
print(arr.index(max(arr)))
print(min(arr))