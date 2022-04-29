"""from tkinter import Y


print("abc.DEF".capitalize())
x=[1,2,10,12,5]
y=x*2
print(abs(len(y)-max(x)))
l1=[1,2,3,4]
l2=l1
l1[2]=5
print(l1)
print(l2)
print(l2==l1)
k=["python","java","kotlin"]
m=[]
for i in k:
    m.append(i[0].upper())
print(m)
a="ispython"
for i in a:
    if i in "kotlin":
        print(a[1],end="")

a=[1,2,3,4,5]
b=[1,2,3,4,5,5]
print(a==b,end="")
print(set(a)==set(b))

i=2,10
j=3,5
add=i+j
print(add)

a=[1,2,3,4,5]
for i in a:
    if i+1!=len(a):
     print(i)
    
python={1:"python",2:"html"}
print("html" in python)
a=list(map(int,input().split(',')))
n1=len(a)
n2=n1//2
su=sum(a)/2
dp=[[-1 for i in range(n2+1)] for j in range(n1)]
def answer(i,n,s):
 if i<(n-1):
  return float('inf')
 if n==0:
  return abs(s)
 else:
  return min(answer(i-1,n-1,s-a[i-1]),answer(i-1,n,s))

k=answer(n1-1,n2,su)
print(int(su-k),int(su+k))"""
s=9
print(type(s))