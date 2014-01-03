#using sieve of eratosthenes http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

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


a = primes_sieve(10001,10000000)
print a[10000] #10001st number is 10000 index
