n=str(input("enter a number:"))
lis=list(n)
out=list()
for il in lis:
    a=int(il)
    if(a==9):
      out.append('0')
      continue
    a=a+1
    b=str(a)
    out.append(b)
a="".join(out)    
print(a)      
