#Max of Three Numbers 
num1=int(input("Enter first Numbers:"))
num2=int(input("Enter second Numbers:"))
num3=int(input("Enter third Numbers:"))
def Find_Max(num1,num2,num3):
    if num1>num2 and num1>num3:
        max = num1
    elif num2>num1 and num2>num3:
        max=num2
    else:
        max=num3
    return max
print("The maximum is :",Find_Max(num1,num2,num3))
