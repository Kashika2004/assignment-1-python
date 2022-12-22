gross_income = float(input("ENTER THE GROSS INCOME: "))
number_of_dependents = float(input("ENTER NO. OF DEPENDENTS: "))
# standard deduction = $10000, dependent deduction = $3000
taxable_income = gross_income - 10000-(3000 + number_of_dependents)
tax=taxable_income*0.20
print( "TAX =$",tax)