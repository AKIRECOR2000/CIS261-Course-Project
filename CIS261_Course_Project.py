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
     

def printInfo(name, hours, hourly_rate, gross, tax_rate, income_tax, net_pay):
    print(name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")
    
def totals():
    print(f"\nTotal Employees:{total_employees}")
    print(f"Total Hours: {total_hours:,.2f}")
    print(f"Total Gross Pay: {totalGross_pay:,2f}")
    print(f"Total Taxes: {total_tax:,.2f}")
    print(f"Total Net Pay: {total_netpay:.2f}")
    
if __name__ == "__main__":
    total_employees = 0
    total_hours = 0.00
    totalGross_pay = 0.00
    total_tax = 0.00
    total_netpay = 0.00
    while True:
        name = empName()
        if (name.upper() == "EXIT"):
            break
        hours = hours_worked()
        hourly_rate = hourlyRate()
        tax_rate = taxRate()
        gross, income_tax, net_pay = TaxAndNet(hours, hourly_rate, tax_rate)
        
        printInfo(name, hours, hourly_rate, gross, tax_rate, income_tax, net_pay)
        
        total_employees += 1
        total_hours += hours
        totalGross_pay += gross
        total_tax += income_tax
        total_netpay += net_pay
    
    totals(total_employees, total_hours, totalGross_pay, total_tax, total_netpay)
    
    
                 
