#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Thu Jan 21 17:18:14 2016
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
__date__ = 'Thu Jan 21 17:18:14 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


def inverseDecimals(n, maxLength=3000):

    if n <= 1:
        raise ValueError("Works only for integers > 1")

    result = []
    rest = 1
    repeatLength = 0
    repeating = False

    while rest != 0 and len(result) <= maxLength and not repeating:

        q, rest = divmod(rest, n)
        rest *= 10
        result.append(q)

        # check if repeating
        if sum(result) > 0:

            resultCopy = result[:]

            while resultCopy[0] == 0:

                length = len(resultCopy)/3

                if resultCopy[-3*length:-2*length] ==\
                   resultCopy[-2*length:-length] == resultCopy[-length:]:

                    repeatLength = max([length, repeatLength])
                    repeating = True

                del resultCopy[0]

            if repeating:

                del result[-2*repeatLength:]
                break

    if len(result) < maxLength and not repeating:

        floatnum = ''.join(map(str, result))
        floatnum = float(floatnum[0] + '.' + floatnum[1:])
        assert floatnum * n == 1, "n = {}".format(n)

    return result, repeatLength


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    maxRepeat = 0

    for i in xrange(2, 1000):

        div = inverseDecimals(i)

        if div[1] > maxRepeat:

            maxRepeat = div[1]
            print i, div[1]

# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
