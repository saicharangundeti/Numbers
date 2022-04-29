num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result1=0
result2=0
for i in range (1,num1):
    if num1%i==0:
       result1+=i
for i in range(1,num2):
    if num2%i==0:
        result2+=i
if result1==num2 and result2==num1:
    print("Amicable pair")
else:
    print("not amicable pair")