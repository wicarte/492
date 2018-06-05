#Assignment 2 (W3D4) - William Carter
hours = int(input("Please enter the number of hours: "))
rph = int(input("Please enter the rate per hour: "))
if hours <= 40:
	total = hours*rph
else:
	total = 40*rph + (hours - 40)*1.5*rph
print "Gross pay: ", total

	
