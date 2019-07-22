num=int(input("Enter the value of n:"))
sum=0
def compute(a):
    global sum
    sum=sum+a
for i in range(2,num+1):
    a=1/(i**3)
    compute(a)
print(sum)    
 


