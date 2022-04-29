#To check whether the number is palindrom or not 
def palindrom():
    number = int(input("Enter a number to check whether it is palindrom or not: "))
    temperary = number 
    new_number = 0
    while temperary !=0: 
        reminder = temperary % 10
        new_number = new_number *10+reminder
        temperary = temperary // 10
    if number == new_number :
        print("Number is a Palindrom")
    else:
        print("Number is not a Palindrom")
palindrom()