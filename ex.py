def amstrong_num(num):
    num_1=num
    res=0
    while num != 0:
        r=num % 10
        res=res + r ** 3
        num=num //10
    return num_1 == res    
input_num=int(input("enter the number:")) 
if amstrong_num(input_num):
    print(f"given number {input_num} is an amstrong")   
else:
    print(f"given number {input_num} is not an amstrong")       