#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Tue Jan 19 17:00:13 2016
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
__date__ = 'Tue Jan 19 17:00:13 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


def numberString(n):

    strings = {1: "one",
               2: "two",
               3: "three",
               4: "four",
               5: "five",
               6: "six",
               7: "seven",
               8: "eight",
               9: "nine",
               10: "ten",
               11: "eleven",
               12: "twelve",
               13: "thirteen",
               15: "fifteen",
               18: "eighteen",
               20: "twenty",
               30: "thirty",
               40: "forty",
               50: "fifty",
               80: "eighty",
               100: "hundred",
               1000: "thousand"}

    if n in strings and n < 100:

        return strings[n]

    else:

        result = ''
        rest = n

        # get thousands
        thousands = rest / 1000
        rest -= thousands*1000

        if thousands > 0:

            result += strings[thousands] + strings[1000]

        # get hundreds
        hundreds = rest / 100
        rest -= hundreds*100

        if hundreds > 0:

            result += strings[hundreds] + strings[100]

        if rest > 0:

            if result != '':
                result += "and"

            if rest in strings:
                result += strings[rest]
                rest = 0

            tens = rest / 10
            rest -= tens*10

            if tens > 1:

                if tens*10 in strings:
                    result += strings[tens*10]
                else:
                    result += strings[tens] + "ty"

                if rest > 0:
                    result += strings[rest]

            elif tens == 1:

                if rest > 0:
                    result += strings[rest] + "teen"

            else:

                if rest > 0:
                    result += strings[rest]

        return result


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    theString = ''

    for i in xrange(1, 1001):
        theString += numberString(i)

    print len(theString)

# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
