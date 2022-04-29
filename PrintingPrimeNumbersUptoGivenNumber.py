#To print prime numbers upto given numbers
number=int(input("Enter a number to print prime numbers upto the given numbers: "))
print("The prime numbers are : ")
for i in range(1,number):
    count = 0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count == 1:
        print(i,end="  ") 