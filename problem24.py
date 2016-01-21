#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Thu Jan 21 14:07:46 2016
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
__date__ = 'Thu Jan 21 14:07:46 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


def permutations(array):

    if len(array) == 1:
        yield array

    array = sorted(array)

    for i, val in enumerate(array):
        for perm in permutations(array[:i] + array[i+1:]):
            yield [val] + perm


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    i = 1

    for perm in permutations(range(10)):

        if i == 1000000:

            print perm
            break

        else:
            i += 1


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
