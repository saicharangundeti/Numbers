#To print numbers from 1 to 100 which are not divisible by 3 or 5
for i in range(100):
    if i%3 == 0  or i%5 == 0:
        continue
    else:
        print(i,end=" ")