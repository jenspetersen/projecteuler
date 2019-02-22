#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:AUTHOR: Jens Petersen
:ORGANIZATION: Heidelberg University Hospital; German Cancer Research Center
:CONTACT: jens.petersen@dkfz-heidelberg.de
:SINCE: Fri Jan 22 14:02:15 2016
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
__date__ = 'Fri Jan 22 14:02:15 2016'
__version__ = '0.1'


# =============================================================================
# METHODS
# =============================================================================

def get_combinations(target, options):

    options = sorted(options, reverse=True)

    if len(options) == 0 or min(options) > target or target <= 0:
        yield []

    for o, option in enumerate(options):

        if option > target:
            continue

        for combination in get_combinations(target - option, options[o:]):
            yield [option] + combination


# =============================================================================
# MAIN METHOD
# =============================================================================

def main():

    options = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    all_combinations = list(get_combinations(target, options))
    print(len(all_combinations))


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    main()
