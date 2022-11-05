#User input 
n1 = int(input())
n2 = int(input())
#Compare n1 and n2
if n1 > n2:
	#Print error message
	print("Second integer can't be less than the first.")
else:
	#Compute result 
	while n1 <= n2:
		#Output result 
		print(n1, end=' ')
		#Increment
		n1 += 5
	#Print new line 
	print()

