#Finbonacci Series 
def fib(last_number): 
    if last_number < 0 :
        print("Entered number is not a positive number.")
    else:
        first_number = 0
        if last_number < 1:
            print(first_number)
        else:
            second_number = 1
            print(first_number,second_number,end=" ") 
            next_number=first_number+second_number
            while next_number < last_number:
                print(next_number,end=" ")
                first_number = second_number
                second_number = next_number
                next_number = first_number+second_number
last_number=int(input("Enter the last Number: "))
fib(last_number)