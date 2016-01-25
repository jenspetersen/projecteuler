#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Fri Jan 22 12:47:24 2016
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
__date__ = 'Fri Jan 22 12:47:24 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    sum_ = 1
    number = 1001

    for n in xrange(3, number + 1, 2):

        sum_ += 4*n**2 - 6*(n - 1)

    print sum_


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()

