#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Wed Jan 20 11:14:42 2016
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
__date__ = 'Wed Jan 20 11:14:42 2016'
__version__ = '0.1'

# =============================================================================
# CLASSES
# =============================================================================


# =============================================================================
# METHODS
# =============================================================================


def isLeapYear(year):

    if year % 400 == 0:
        leapYear = True
    elif year % 100 == 0:
        leapYear = False
    elif year % 4 == 0:
        leapYear = True
    else:
        leapYear = False

    return leapYear


def weekday(year, month, day):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday"]

    # get difference to 01/01/1990
    difference = 0

    for y in xrange(1900, year):

        if isLeapYear(y):
            difference += 366
        else:
            difference += 365

    for m in range(1, month+1):

        if m == 2:

            if isLeapYear(year):
                difference += 29
            else:
                difference += 28

        else:

            if m % 2 == 0 and m >= 8:
                difference += 31
            elif m % 2 == 0:
                difference += 30
            elif m >= 8:
                difference += 30
            else:
                difference += 31

    difference += day

    return days[difference % 7 - 1]


# =============================================================================
# MAIN METHOD
# =============================================================================


def main():

    sundayCount = 0

    for y in xrange(1901, 2001):
        for m in range(1, 13):
            print y, m, 1
            if weekday(y, m, 1) == "Sunday":
                sundayCount += 1

    print sundayCount


# =============================================================================
# RUN
# =============================================================================


if __name__ == "__main__":

    main()

