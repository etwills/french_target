import math

"""
Gives the first n primes
Assumptions:
- n is greater than 1, that is we don't just want the first prime 2
"""
def compute_n_primes(n):
    primes = [2]
    num_found = 1
    k = 3
    while num_found < n: 
        # check if k is prime
        if is_prime(k):
            primes.append(k)
            num_found += 1
        k += 2    
    return primes

def is_prime(num):
    # check until the square root of num
    for i in range(2, math.ceil(math.sqrt(num))):
        # if there is a divisor
        if num%i == 0:
            return False
    return True        