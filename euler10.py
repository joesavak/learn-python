#using sieve of eratosthenes http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def primes_sieve(index,limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    sumN=0
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)
        sumN+=i	
    return sumN


a = primes_sieve(10001,2000000)
print(a)
