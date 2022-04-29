from fractions import Fraction
"""
x=int(input())
y=int(input())
a=int(input())
b=int(input())
print(Fraction(x,y)+Fraction(a,b))
print(Fraction(x,y)-Fraction(a,b))
print(Fraction(x,y)*Fraction(a,b))
print(Fraction(x,y)/Fraction(a,b))
print(pow(x,0.5)"""
n=int(input("Enter the number of elements: "))
array=[]
for i in range(n):
    x=int(input("enter numerator: "))
    y=int(input("Enter denominator: "))
    t=x/y
    array.append(t)
array.sort()
print(array)