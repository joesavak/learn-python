def div_by_all(num):
    for j in range(20,2,-1):
        if(num%j)!=0:
            return False
    return True

found = 0
y = 1
#380 is product of 19 and 20- used to speed it up and not sure if this
#method would work for others.
while(found==0):
    n= y*380
    y+=1
    print(n)
    if div_by_all(n):
        found=1
print(y)
