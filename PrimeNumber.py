import math

x=10000
def sosu(s):
	a=int(math.sqrt(s))
	for i in range(2,a):
		if s%i==0:
			return False
	return True
while 1:
	if sosu(x):
		print(x)
	x=x+1
