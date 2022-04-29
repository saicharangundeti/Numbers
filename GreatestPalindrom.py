
def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)
num1=int(input("Enter a number :"))
temp=num1
result=0
while temp!=0:
    n= temp%10
    result+=Factorial(n)
    temp=temp//10
if result == num1:
    print("It is a strong number ")
else:
    print("It is not a strong number")