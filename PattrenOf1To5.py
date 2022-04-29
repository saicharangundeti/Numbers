"""print("For outer iterator ")
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

print("for in iterator ")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        if col==0  or row==(n-1) or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
for row in range(4):
    for col in range(7):
        if row==3 or col+row==3 or col-row==3:
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
