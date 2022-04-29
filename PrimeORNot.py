#prime number or not
def check_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
number=int(input("Enter a number to check it is a prime : "))
if check_prime(number) == True :
    print("Yes, It is prime")
else:
    print("No, It is not a prime")