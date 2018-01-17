# Payroll

# get name, hours, pay, cpf
name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
payrate = int(input("Enter hourly pay rate in $: "))
cpf =int(input("Enter CPF contribution rate in %: "))

# compute grosspay, contri, netpay
grosspay = hours * payrate
contri = ( cpf / 100 ) * grosspay
netpay = grosspay - contri

# display result
print()
print("Payroll statement for", name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate: $", payrate)
print("Gross pay: $", grosspay)
print("CPF Contribution at {0}%: ${1}".format(cpf, contri))
print("Net pay: $", netpay)
