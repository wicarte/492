#Assignment 3 (W3D4) - William Carter

#What I think will happen before running the code:
#I think the code prompts the user to enter a number, casts
#the number as an int, counts up by 1 on the interval (2, user
#provided number), and prints whenever the outer loop iterator (i)
#is not cleanly divisible by the inner loop iterator (k).

n = input("Please enter a number as an upper limit: ")
n = int(n)

for i in range(2, n):
	check_var = True
	for k in xrange(2, i):
		if (i%k) == 0:
			check_var = False
		if check_var:
			print(i)

#After running the code:
#A number is printed out and another number is printed out as many times
#as the first number's value. For example, if 5 is printed out and 7
#is the next number to be printed, 7 will print 5 different times. 
#This pattern continues until the upper bound provided by the user 
#is reached.
