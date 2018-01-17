# Computing the volume of a cylinder

# get radius and length
print("Enter the radius and length of a cylinder to find out its volume.")
radius = float(input("Radius: "))
length = float(input("Length: "))

# pi
pi = 3.14159

# compute area
area = radius * radius * pi

# compute volume
volume = area * length

# display volume
print("The volume of the cylinder is {0:.2f}.".format(volume))
