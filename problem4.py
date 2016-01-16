#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Tue Jan 12 10:11:53 2016
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
__date__ = 'Tue Jan 12 10:11:53 2016'
__version__ = '0.1'

# =============================================================================
# CLASSES
# =============================================================================


# =============================================================================
# METHODS
# =============================================================================


def ispalindrome(number):

    string = str(number)
    result = True

    for i in range(len(string)/2):
        if not string[i] == string[-(i+1)]:
            result = False

    return result


def findpalindrome(lower, upper, limit=0):

    for i in reversed(xrange(lower, upper+1)):
        for j in reversed(xrange(lower, upper+1)):
            k = i*j
            if ispalindrome(k) and k > limit:
                return j, i, k

    return 1, 1, 0

# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    lower, upper, palindrome = 1, 1000, 0

    while True:

        lower, upper, current = findpalindrome(lower, upper-1, palindrome)
        print lower, upper, current

        if current > palindrome:
            palindrome = current
        else:
            break

    print palindrome

# =============================================================================
# RUN
# =============================================================================


if __name__ == "__main__":

    main()
