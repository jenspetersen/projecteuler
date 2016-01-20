#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Tue Jan 19 14:19:57 2016
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

import operator

# =============================================================================
# PROGRAM METADATA
# =============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Tue Jan 19 14:19:57 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================



# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    collatzLengths = {1: 1}

    for i in xrange(2, 1000000):

        length = 0
        j = i

        while True:

            if j in collatzLengths:

                length += collatzLengths[j]
                collatzLengths[i] = length
                break

            else:

                length += 1
                if j % 2 == 0:
                    j = j/2
                else:
                    j = 3*j + 1

    maxkey = max(collatzLengths.iteritems(), key=operator.itemgetter(1))
    print maxkey

# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
