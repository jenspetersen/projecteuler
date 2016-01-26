#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Tue Jan 26 17:52:07 2016
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


# =============================================================================
# PROGRAM METADATA
# =============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Tue Jan 26 17:52:07 2016'
__version__ = '0.1'

# =============================================================================
# ClASSES
# =============================================================================


# =============================================================================
# METHODS
# =============================================================================


def permutations(string):

    if len(string) == 1:
        yield string

    for i, s in enumerate(string):
        for p in permutations(string[:i] + string[i+1:]):
            yield s + p


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    products = set([])

    for p in permutations("123456789"):

        if int(p[0]) * int(p[1:5]) == int(p[5:]):
            print "{} x {} = {}".format(p[0], p[1:5], p[5:])
            products.add(int(p[5:]))

        if int(p[:2]) * int(p[2:5]) == int(p[5:]):
            print "{} x {} = {}".format(p[:2], p[2:5], p[5:])
            products.add(int(p[5:]))

    print sum(products)

# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
