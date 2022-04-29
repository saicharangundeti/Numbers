#To Check Whether The Number Is Amstrong Or Not
from token import NUMBER


def Amstrong(x):
    n=len(str(x))
    temp=x
    result=0
    while temp>0:
        rem=temp%10
        result=result+rem**n
        temp=temp//10
    if x==result:
        print("It is a Amstrong number")
    else:
        print("It is not a Amstrong number")

num=int(input("Enter a number : "))
Amstrong(num)