#Factorial
def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)
number=int(input("Enter a number to find its factorial: "))
print(Factorial(number))