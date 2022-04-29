#Sum of Pairs in a array 
arr=[]
n=int(input())
for i in range(n):
    ele=int(input())
    arr.append(ele)
x=int(input())
flag = 1 
for j in range(n):
    temp=arr[j]
    for k in range(j+1,n):
        if temp+arr[k]==x:
            print("Pair with a given sum %d is (%d,%d)"%(x,temp,arr[k]))
            flag==0                 
if flag==0:
    print("No Valid Pair Exits")