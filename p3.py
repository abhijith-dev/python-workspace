num=int(input("Enter a number:"))
is_prime=True
if num<2:
    is_prime=False
else:
    for i in range(2,num//2+1):
        if num%i==0:
            is_prime=False
            break
if(is_prime):
    print(num," a prime number") 
else:
    print(num," a not prime number")                   