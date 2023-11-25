#Akire Cormier, CIS261, Course Project
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
     
def printInfo(EmpDetailList):
    total_employees = 0
    total_hours = 0.00
    totalGross_pay = 0.00
    total_tax = 0.00
    total_netpay = 0.00
    for empList in detail_list:
        startDate = empList[0]
        endDate = empList[1]
        name = empList[2]
        hours = empList [3]
        hourly_rate = empList [4]
        tax_rate = empList [5]
    
        gross, income_tax, net_pay = TaxAndNet(hours, hourly_rate, tax_rate)
        print(startDate, endDate, name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")
        
        total_employees += 1
        total_hours += hours
        totalGross_pay += gross
        total_tax += income_tax
        total_netpay += net_pay
        
        emp_totals["totEmp"] = total_employees
        emp_totals["totHours"] = total_hours
        emp_totals["totGross"] = totalGross_pay
        emp_totals["totTax"] = total_tax
        emp_totals["totNet"] = total_netpay

def totals():
    print(f'Total Employees:   {emp_totals["totEmp"]}')
    print(f'Total Hours:    {emp_totals["totHours"]}')
    print(f'Total Gross Pay:    {emp_totals["totGross"]}')
    print(f'Total Taxes:    {emp_totals["totTax"]}')
    print(f'Total Net Pay:    {emp_totals["totNet"]}')
    
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
    detail_list = []
    emp_totals = {}
    while True:
        name = empName()
        if (name.lower() == "end"):
            break
        startDate, endDate = datesWorked()
        hours = hours_worked()
        hourly_rate = hourlyRate()
        tax_rate = taxRate()
        
        print()
        
        EmpDetail = [startDate, endDate, name, hours, hourly_rate, tax_rate]
        
        write_empInfo(EmpDetail)
        
    print()
    print()
    startDate = get_fromDate()
    
    EmpDetailList = Read_empInfo(startDate)
    
    print()
    printInfo(EmpDetailList)
    print()
    totals()
    
                 
