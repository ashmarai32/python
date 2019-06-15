string=input("enter a string")
l=len(string)
stringr=''
i=0
while(i<l):
    stringr=string[i]+stringr
    i=i+1

if(stringr==string):
    print("palindrome")
else:
    print("not")
print(stringr)

        
