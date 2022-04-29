number=input()
otp=''
for i in range(1,len(number),2):
    odd=int(number[i])
    sq_odd_number=odd**2
    otp+=str(sq_odd_number)
print(otp[:4])