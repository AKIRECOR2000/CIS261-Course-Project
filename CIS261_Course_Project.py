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
     
def printInfo(detail_list):
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
        empDetail = []
        empDetail.insert(0, startDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, name)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourly_rate)
        empDetail.insert(5, tax_rate)
        detail_list.append(empDetail)
    printInfo(detail_list)
    totals()
    
    
                 
