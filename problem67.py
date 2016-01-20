#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Wed Jan 20 10:32:32 2016
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
__date__ = 'Wed Jan 20 10:32:32 2016'
__version__ = '0.1'

# =============================================================================
# METHODS
# =============================================================================


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    triangle = []

    with open("problem67.txt", 'r') as triangleFile:

        for line in triangleFile:

            line.replace('\n', '')
            line = line.split(' ')
            triangle.append(map(int, line))

    maxScores = collections.deque([])

    while len(triangle) > 0:

        currentLine = triangle.pop()

        if len(maxScores) == 0:

            maxScores.append(currentLine)

        else:

            scores = []

            for i, value in enumerate(currentLine):

                scores.append(value + max(maxScores[0][i:i+2]))

            maxScores.appendleft(scores)

    print maxScores[0]

# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
