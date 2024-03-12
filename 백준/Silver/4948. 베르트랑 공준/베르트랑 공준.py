import sys

MAX_NUM = 123456 * 2 + 1

def sieve_of_eratosthenes():
    primes = [True] * MAX_NUM
    primes[0] = primes[1] = False

    for i in range(2, int(MAX_NUM ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, MAX_NUM, i):
                primes[j] = False

    return [i for i in range(MAX_NUM) if primes[i]]

primes = sieve_of_eratosthenes()

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    count = sum(1 for prime in primes if num < prime <= num * 2)
    print(count)
