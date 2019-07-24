from employee import Employee

lst_emp=[]

def load_emp():
    with open("empdata.txt") as f:
        fdata=f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno=int(edata[0])
            ename=edata[1]
            qual=edata[2]
            salary=int(edata[3])
            dept_name=edata[4]
            emp=Employee(empno,ename,qual,salary,dept_name)
            lst_emp.append(emp)
    print(f"total Employee count:{len(lst_emp)}")

def showDeptName():
    dept_name=set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dept_name:
        print(name)

def showAllQualifications():
    qual=set(map(lambda emp:emp.qual,lst_emp))
    for qual in qual:
        print(qual)

def maxSalaryEmp():
    max_salary=max(list(map(lambda x:x.salary,lst_emp)))
    lst=list(filter(lambda x:x.salary==max_salary,lst_emp))
    for emp in lst:
        emp.show_info()
def showEmpCountByDeptName():
    pass
def showTotalSalByDeptName():
    pass
def showEmpCountByQual():
    pass





load_emp()
print("all department names:")
showDeptName()
print("all qualifications:")
showAllQualifications()
maxSalaryEmp()