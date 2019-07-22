num=int(input("Enter the value of n:"))
sum=0
def compute(a):
    global sum
    sum=sum+a
for i in range(1,num+1):
    a=1/i
    compute(a)
print(sum)    
 


