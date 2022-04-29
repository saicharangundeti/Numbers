#To Find the LCM of TWO Numbers
def lcm():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if num1 == 0 or num2 == 0:
        print("No LCM exit for 0")
    else:
        if num1>num2:
            max=num1
        else:
            max=num2
        while 1: 
            if max%num1==0 and max%num2==0:
                print("LCM of Given numbers is = ",max)
                break
            max+=1    
lcm()
