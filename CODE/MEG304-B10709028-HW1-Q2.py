#!/usr/bin/env python
# coding: utf-8

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2

    while (p * p <= n):

        # If prime [p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            print(p, end=" ")


# driver program
n = 30
print(f"Following are the prime numbers smaller than or equal to {n}")
SieveOfEratosthenes(n)


# driver program
n = 45
print(f"Following are the prime numbers smaller than or equal to {n}")
SieveOfEratosthenes(n)


# driver program
n = 111
print(f"Following are the prime numbers smaller than or equal to {n}")
SieveOfEratosthenes(n)

