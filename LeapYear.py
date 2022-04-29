year=int(input("Enter year to check leap year or not: "))
if year%100==0 and year%400==0:
    print("Leap year")
elif year%4 == 0:
        print("leap year")
else:
        print("non leap year")