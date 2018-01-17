# Summing the digits in an integer

# get integer
integer = int(input("Input an integer of up to four digits: "))

# extract digits
x  = integer //1000
x1 = (integer - x*1000)//100
x2 = (integer - x*1000 - x1*100)//10
x3 = integer - x*1000 - x1*100 - x2*10

# sum digits
sum = x+x1+x2+x3

# display result
print("The sum of digits in the number is {0}.".format(sum))
