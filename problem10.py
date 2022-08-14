# computing primes with Sieve of Eratosthenes
def primes_sieve(num):
    max = num+1
    aux = [True] * max
    for i in range(2, int(num**0.5 + 1)):
        if aux[i]:
            for j in range(i*i, max, i):
                aux[j] = False
    primes = []
    for i in range(2, max):
        if aux[i]:
            primes.append(i)
    return primes


print(sum(primes_sieve(2000000)))
