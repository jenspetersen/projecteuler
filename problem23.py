#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Thu Jan 21 11:45:17 2016
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
__date__ = 'Thu Jan 21 11:45:17 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


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


def divisors(n):

    if n == 0:
        return set([])

    if n == 1:
        return set([1])

    result = allProducts(primeFactors(n))
    result.remove(n)
    result.add(1)
    return result


def allTwoSums(summands):

    result = set([])

    for i, value in enumerate(summands):

        sums = map(lambda x: x+value, summands[i:])
        result.update(sums)

    return result


def quality(n):

    sumOfDigits = sum(list(divisors(n)))

    if sumOfDigits > n:
        return "abundant"

    elif sumOfDigits == n:
        return "perfect"

    else:
        return "nonabundant"


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    abundant = []

    for i in xrange(1, 28124):
        if quality(i) == "abundant":
            abundant.append(i)

    numbers = set(range(1, 28124))
    numbers -= allTwoSums(abundant)

    print sum(numbers)


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
