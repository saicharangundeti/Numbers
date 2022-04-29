num1 = int(input("Enter a number : "))
square=num1**2
count=0
while num1 > 0:
    if (num1%10 != square%10 ):
        count=1
        print("Not automarphic number")
        break
    num1//10
    square//10
if count == 0:
    print("Automorphic")