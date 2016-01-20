#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Wed Jan 20 11:54:41 2016
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
__date__ = 'Wed Jan 20 11:54:41 2016'
__version__ = '0.1'

# =============================================================================
# CLASSES
# =============================================================================


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

    return allProducts(primeFactors(n))


# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    pairs = []

    for i in range(1, 10000):

        div = divisors(i)
        div.add(1)
        div.remove(i)
        s = sum(list(div))

        if s != 0:

            div2 = divisors(s)
            div2.add(1)
            div2.remove(s)
            s2 = sum(list(div2))

            if s2 == i and i != s and s < 10000 and (s, i) not in pairs:

                print i, s
                pairs.append((i, s))

    print sum(map(sum, pairs))

# =============================================================================
# RUN
# =============================================================================


if __name__ == "__main__":

    main()
