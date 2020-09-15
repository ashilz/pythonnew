f=open("employeesdata","r")
emp={}
for lines in f:
    id,name,desig,salary=lines.rstrip("\n").split(",")
    if(id not in emp):
        emp[id]={"id":id,"name":name,"desig":desig,"sal":salary}

def fetchdata(**kwargs):
    id=kwargs["id"]
    if(id not in emp):
        print("emp not exist")
    else:
        print(emp[id]["name"])  # kwargs is a dict
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])


fetchdata(id="1002",prop="desig")
