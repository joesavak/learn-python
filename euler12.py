def get_triang(n):
	triang=0
	for i in range(1,n+1):
		triang+=i
	return triang




def primes_sieve(index,limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)
	if len(primes) >= index+1:
		return primes #return quick once index found
    return primes


a = primes_sieve(250,100000)
for x in range(2,100000000):
	t= get_triang(x)
	divs = 1
	sums = 1
	#print "x::" + str(x)
	for prindex in range (0,len(a)):
		#print "**prime ::" + str(a[prindex])
		#print "**sums ::" + str(sums)
		#print "**divs :: " + str(divs)
		if sums == x:
			break		
		if a[prindex] == x or (a[prindex] + sums) == x:
			#print "--prime equals x or prime & sums equals x"
			sums*=a[prindex]
			divs *= 2
			break
		if a[prindex] > x:
			#print "--prime greater than x"
			break
		if (x % a[prindex]) == 0:
			#print "-- x divisible by prime"			
			for j in range (0,1000): 
				exp = a[prindex]**j
				#print "-- testing prime to the " + str(j)
				#print "-- exp: " + str(exp)
				if (x % exp) != 0: #found a prime that breaks the sum mod rule. Need prev prime
					#print "-- found break where x % exp not 0"
					sums*=a[prindex]**(j-1)
					#print "----- sums:" + str(sums)
					divs*=(j)
					#print "----- divs:" + str(divs)					
					break
					
				if x == (sums+exp):
					#print "-- found break where x = sums+exp"
					sums*=exp
					if a[prindex] == 1:
						divs*=2
					else: 
						divs*=(j+1)
					print "----- divs:" + str(divs)
					break
				if exp > x:
					#print "-- found break where exp > x"
					break

					
				

	
	if divs > 500:
		print str(x) + ":: num divs:: " + str(divs)
		break
			




