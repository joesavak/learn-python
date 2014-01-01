k=0
#optimization ideas: check to see if both mods are being done or if it stops at first failure.
#better to use diff loop?
for x in range (3,1000):
	if (x%3==0) or (x%5==0):
		k=k+x
	x+=1
print(k)