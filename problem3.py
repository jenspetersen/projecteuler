#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Mon Jan 11 12:03:11 2016
:VERSION: 0.1

DESCRIPTION
-----------



REQUIRES
--------



TODO
----



"""
# ==============================================================================
# PROGRAM METADATA
# ==============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Mon Jan 11 12:03:11 2016'
__version__ = '0.1'

# ==============================================================================
# IMPORT STATEMENTS
# ==============================================================================

from numpy import sqrt

# ==============================================================================
# METHODS
# ==============================================================================


def primefactors(n):

    if n % 2 == 0:
        yield 2
        for factor in primefactors(n / 2):
            yield factor

    else:
        for i in xrange(3, n+1, 2):
            if n % i == 0:
                yield i
                for factor in primefactors(n / i):
                    yield factor
                break

# ==============================================================================
# MAIN METHOD
# ==============================================================================


def main():

    print max(primefactors(600851475143))

# ==============================================================================
# RUN
# ==============================================================================

if __name__ == "__main__":

    main()
