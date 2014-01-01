num=600851475143
def is_prime(num):
	for x in range(2,num):
		if (num % x) == 0:
			return False
	return True
#opt ideas: split into threads, check mod [3,5]. 

for y in range(2,int(num/2)):
	#print("checking:"+str(y))
	if (y%2==0):
		continue
	if (num%y)!=0:
		continue
	if is_prime(y):
		top=y
		print(top)

	