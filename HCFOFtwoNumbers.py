#To Find HCF of Two Numbers 
def hcf():
    num1=int(input("Enter the  first number: "))
    num2=int(input("Enter the second number: "))
    if num1==0 or num2==0:
        print("No HCF for 0")
    else:
        if num1<num2:
            min=num1
        else:
            min=num2
        while min!=0:
            if num1%min==0 and num2%min==0:
                print(min)
                break
            min-=1
hcf()