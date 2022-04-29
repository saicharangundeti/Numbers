"""num = int (input())
count=0
for i in range(1,num):
    if num%i==0:
        count+=1
if count==1:i
    print("prime")
else:
    print("not prime")
num1=0
num2=1
num=int(input())
result=0
while result < num:
    print(result,end=" ")
    num1=num2
    num2=result
    result=num1+num2
n=int(input())
for i in range(1,n):
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count == 1:
        print(i)"""

string=input()
element_list=string.split(",")
final_string=""
for ele in element_list:
    sub_list=ele.split(":")
    name=sub_list[0]
    code=sub_list[1]
    name_length=len(name)
    max=0
    for i in code:
        if int(i)<=name_length:
            if max<int(i):
                max=int(i)
    if max==0:
        final_string += "X"
    else:
        final_string += name[max-1]
print(final_string)

































