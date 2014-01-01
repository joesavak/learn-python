answer=0
prevVal=0
nextVal=1
sumVals=0
while(sumVals<=40000000):
	sumVals=prevVal+nextVal
	if (sumVals%2==0) and (sumVals<=4000000):
		answer=answer+sumVals
	prevVal=nextVal
	nextVal=sumVals
print(answer)
