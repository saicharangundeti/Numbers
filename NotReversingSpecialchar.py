#Reversing a String keeping special charecters at same position
import re
string=input()
alphabets=re.findall("[a-zA-Z]",string)
alphabets.reverse()
for i in range(len(string)):
    if not (string[i].isalpha()):
        alphabets.insert(i,string[i])
print("".join(alphabets))