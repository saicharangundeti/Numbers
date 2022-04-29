#perfect number or not 
n=int(input("Enter a number to check wherther it is perfect number or not: "))
def Perfect(x):
    result=0
    for j in range(1,x):
        if x%j==0:
            result=result+j
    if result==x:
        print("It it a perfect number")
    else:
        print("It is not a perfect number")
Perfect(n)        