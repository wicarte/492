print("Enter three numbers\n")
x = input("Enter first number: ")
y = input("Enter second number: ")
z = input("Enter third number: ")
list = []
xOdd = x % 2
yOdd = y % 2
zOdd = z % 2

if xOdd != 1:
	list.append(x)
if yOdd == 1:
	list.append(y)
if zOdd == 1:
	list.append(z)
list.sort()
print(list.pop())
