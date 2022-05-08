# Conut Of Number of piars equals to sum
arr=[]
n=int(input())
for i in range(n):
    ele=int(input())
    arr.append(ele)
x=int(input())
count=0
for j in range(n):
    temp=arr[j]
    for k in range(j+1,n):
        if temp+arr[j+1]==x:
            count+=1
print(count)            