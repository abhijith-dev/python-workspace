lst=[]
def add(ele):
    lst.append(ele)
def pop():
    if len(lst)==0:
        print("list empty!")
    else:
        ele=lst.pop()
        print(f"element {ele} removed")
def search(ele):
    if len(lst)==0:
        print("list empty!")
    else:
        if ele in lst:
            index=lst.index(ele)
            print(f"element {ele} is found at :{index}")
        else:
            print(f"element {ele} is not found")
def display():
    if len(lst)==0:
        print("list empty!")
    else:
        for i in lst:
            print(i)
while True:
    print("*****1.Add 2.Delete 3.search 4.display 5.Exit*****")
    ch=int(input("enter your choice:"))
    if ch==1:
        ele=int(input("enter the element to add:"))
        add(ele)
    elif ch==2:
        pop()
    elif ch==3:
        ele=int(input("enter the elements to be search:"))
        search(ele)
    elif ch==4:
        display()
    else:
        break
       
          
