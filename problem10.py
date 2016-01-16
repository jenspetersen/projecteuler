#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Fri Jan 15 10:10:48 2016
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

import collections

# =============================================================================
# PROGRAM METADATA
# =============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Fri Jan 15 10:10:48 2016'
__version__ = '0.1'

# =============================================================================
# CLASSES
# =============================================================================


# =============================================================================
# METHODS
# =============================================================================


# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    # brute force :) slooow

    numbers = range(3, 2000000, 2)
    primeSum = 2

    i = 0

    while i < 2000000:

        try:
            i = numbers.pop(0)
        except IndexError:
            break
        primeSum += i
        print i

        for j, number in enumerate(numbers):
            if number % i == 0:
                del numbers[j]

    print primeSum


# =============================================================================
# RUN
# =============================================================================


if __name__ == "__main__":

    main()
