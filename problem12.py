#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Fri Jan 15 13:57:09 2016
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
import time

# =============================================================================
# PROGRAM METADATA
# =============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Fri Jan 15 13:57:09 2016'
__version__ = '0.1'

# =============================================================================
# CLASSES
# =============================================================================


# =============================================================================
# METHODS
# =============================================================================

def triangle(n):

    return int((n+1) * 0.5 * n)


def primeFactors(n):

    if n in (0, 1):
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


def divisors(n):

    result = [1]

    for i in xrange(2, n/2):
        if n % i == 0:
            result.append(i)

    if n > 1:
        result.append(n)

    return result


def allProducts(factors):

    if len(factors) == 2:
        return set(factors + [factors[0] * factors[1]])

    elif len(factors) == 1:
        return set(factors)

    else:
        result = allProducts(factors[1:])
        for entry in list(result):
            result.add(factors[0] * entry)
        result.add(factors[0])
        return result


# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    divisors = 0
    maxDivisors = 0
    i = 100 # low enough starting point

    while divisors <= 500:

        divisors = len(allProducts(primeFactors(triangle(i))))
        if divisors > maxDivisors:
            maxDivisors = divisors
            print i, triangle(i), divisors

        i += 1

# =============================================================================
# RUN
# =============================================================================


if __name__ == "__main__":

    main()

