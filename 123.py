from functools import reduce
lis=[1,2,3,4,5,6,7,8,9,10]
out=list(map(lambda x:x**2,lis))
out2=list(filter(lambda x:x%2==0,out))
out3=reduce(lambda a,b:a+b,out2)
print(out3)