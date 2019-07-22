import random as r
num=r.randint(1,6)
count=0
while count<3:
    n=int(input("enter your number"))
    if n>num:
        print("guessed number is greater than actual number")
        count=count+1
    elif n==num:
        print("gussed number is correct at ",count,"attempt")
        break
    else:
        print("guessed number is lesser than actual number")
        count=count+1   
if count==3 :
    print("better luck next time")
         
 
