data="Rajesh,Krish,Manoj,Suresh,Jayesh,Mahesh,Charan"
names=data.upper().split(",")

lst=[]
for name in names:
    if name.startswith("A") or name.endswith("H"):
        lst.append(name)
lst.sort()
print(lst)