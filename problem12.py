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

    for i in range(2, n):
        if n % i == 0:
            result.append(i)

    if n > 1:
        result.append(n)

    return result

# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    for i in range(20):
        print i, primeFactors(i)

# =============================================================================
# RUN
# =============================================================================


if __name__ == "__main__":

    main()

