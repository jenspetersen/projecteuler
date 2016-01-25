#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Fri Jan 22 11:28:54 2016
:VERSION: 0.1

DESCRIPTION
-----------



REQUIRES
--------



TODO
----



"""
# =============================================================================
# IMPORT STATEMENTS
# =============================================================================

import numpy as np

# =============================================================================
# PROGRAM METADATA
# =============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Fri Jan 22 11:28:54 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


def primeFactors(n):

    if n <= 1:
        return []

    firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    primes = []
    i = max(firstPrimes) + 2

    for prime in firstPrimes:
        if n % prime == 0:
            return [prime] + primeFactors(n / prime)

    while i < np.sqrt(n):

        isPrime = True

        for prime in firstPrimes + primes:
            if i % prime == 0:
                isPrime = False

        if isPrime:
            if n % i == 0:
                return [i] + primeFactors(n / i)
            else:
                primes.append(i)

        i += 2

    else:

        return [n]

# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    # find primes < 1000
    primes = [2]

    for i in xrange(3, 1000, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    maxScore = 0
    maxA = 0
    maxB = 0

    for b in map(lambda x: -x, primes) + primes:
        for a in xrange(-(b-1), 1000):

            n = 0

            while n < abs(b):
                if len(primeFactors(n**2 + a*n + b)) == 1:
                    n += 1
                else:
                    break

            if n > maxScore:
                maxScore = n
                maxA = a
                maxB = b

    print maxA, maxB, maxScore, maxA*maxB


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
