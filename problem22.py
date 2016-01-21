#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Thu Jan 21 13:37:35 2016
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

import re

# =============================================================================
# PROGRAM METADATA
# =============================================================================

__author__ = 'Jens Petersen'
__email__ = 'jens.petersen@dkfz-heidelberg.de'
__copyright__ = ''
__license__ = ''
__date__ = 'Thu Jan 21 13:37:35 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


def nameScore(name):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0

    for s in name:
        result += alphabet.index(s) + 1

    return result


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    score = 0

    with open("problem22.txt", 'r') as namesFile:

        names = []

        for i, line in enumerate(namesFile):
            names += re.findall("\w+", line)

    names = sorted(names)

    for i, name in enumerate(names):

        score += (i+1) * nameScore(name)

    print score



# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
