#Wap to check a number and check it magical number or not
n=int(input("Enter the number:"))
l=0
s=0
f=0
while n>0:
    l+=1
    c=n%10
    n=n//10
    if(l%2==0):
        s=s+c
    else:
        f=f+c
if(s==f):
    print("Magical number")
else:
    print("Not a magical number")