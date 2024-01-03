def factorial(n):
	if(n==0 or n==1):
		return 1
	else:
		return n*factorial(n-1)

def npr(n,r):
	return factorial(n)/factorial(n-r)
	

n=int(input("Enter value for n: "))
r=int(input("Enter value for r: "))
result=npr(n,r)
print("nPr is",result)	
