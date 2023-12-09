#Akire Cormier, CIS261, Course Project
from datetime import datetime

def create_users():
    print('Create users, passwords, and roles')
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUsername()
        if (username.upper() == "END"):
            break
        userpwd = GetPassword()
        userrole =  UserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUsername():
    username = input("Enter username or 'END' to quit: ")
    return username

def GetPassword():
    pwd = input("Enter password: ")
    return pwd

def UserRole():
    userrole = input("Enter role(Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter a role (Admin or User): ")
            
          
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)
        

def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter username: ")
    UserPwd = input("Enter password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
            UserRole = UserList[2]
            return UserRole, UserName
        
    return UserRole, UserName


def datesWorked():
    startDate = input("Enter the start date in the format of, MM/DD/YYY:")
    endDate = input("Enter the end date in the format of, MM/DD/YYY:")
    return startDate, endDate

def empName():
    name = input("Enter employee's name:")
    return name

def hours_worked(): 
    hours = float(input("Enter hours worked: "))
    return hours

def hourlyRate():
    hourly_rate = float(input("Enter hourly rate:"))
    return hourly_rate

def taxRate():
    tax_rate = float(input("Enter tax rate:"))
    tax_rate = tax_rate / 100
    return tax_rate

def TaxAndNet(hours, hourly_rate, tax_rate):
    gross = hours * hourly_rate
    income_tax = gross * tax_rate
    net_pay = gross - income_tax
    return gross, income_tax, net_pay
     
def printInfo(DetailsPrinted):
    totEmployees = 0
    totHours = 0.00
    totGross_pay = 0.00
    totTax = 0.00
    totNetpay = 0.00
    EmpFile = open("Employees.txt", "r")               
    while True:
        rundate = input("Enter start date for report (mm/dd/yyy) or All for all data: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format, try again.")
            print()
            continue
        
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        EmpList = EmpDetail.split("|")
        startDate = EmpList[0]
        if (str(rundate).upper != "ALL"):
            checkdate = datetime.strptime(startDate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        endDate = EmpList[1]
        name = EmpList[2]
        hours = float(EmpList[3])
        hourly_rate =  float(EmpList[4])
        tax_rate = float(EmpList[5])
        gross, income_tax, net_pay = TaxAndNet(hours, hourly_rate, tax_rate)
        print(startDate, endDate, name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")
        totEmployees += 1
        totHours += hours
        totGross_pay += gross
        totTax += income_tax
        totNetpay += net_pay
        empTotals["TotEmp"] = totEmployees
        empTotals["TotHours"] = totHours
        empTotals["TotGross"] = totGross_pay
        empTotals["TotTax"] = totTax
        empTotals["TotNet"] = totNetpay
        DetailsPrinted = True
        
    if (DetailsPrinted):
        totals(empTotals)
    else:
        print("No information to print.")
       
def totals(empTotals):
    print()
    print(f"Total Employees: {empTotals['totEmp']}")
    print(f"Total Hours: {empTotals['totHours']}")
    print(f"Total Gross Pay: {empTotals['totGross']:,.2f}")
    print(f"Total Taxes: {empTotals['totTax']:,.2f}")
    print(f"Total Net Pay: {empTotals['totNet']:,.2f}")
    
def write_empInfo(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def get_fromDate():
    valid = False
    startDate = ""
    
    while not valid:
        startDate = input("Enter from Date (mm/dd/yyy): ")
        if (len(startDate.split('/')) != 3 and startDate.upper() != 'ALL'):
            print("This format is invalid.")
        else:
            valid = True
    
    return startDate

def Read_empInfo(startDate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    
    if startDate.upper() == 'ALL':
        condition = False
 
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
    
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if startDate == employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList    

if __name__ == "__main__":
    create_users()
    print()
    print("Data Entry")
    UserRole, UserName = Login()
    DetailsPrinted = False
    empTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, " is invalid.")
        
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt:", "a+")
            while True:
                name = empName()
                if (name.upper() == "END"):
                    break
                startDate, endDate = datesWorked()
                hours = hours_worked()
                hourly_rate = hourlyRate()
                tax_rate = taxRate()
                EmpDetail = startDate + "|" + endDate + "|" + name + "|" + str(hours) + "|" + str(hourly_rate) + "|" + str(tax_rate) + "\n"
                EmpFile.write(EmpDetail)
                
            EmpFile.close()
            
        printInfo(DetailsPrinted)
                
                
