names=["PKM","ALN","PVR","PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
c_names={}
for name in names:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]=c_names[name]+1
print(c_names)