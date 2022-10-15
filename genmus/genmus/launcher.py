#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This file contains code to facilitate loading files and running the program. """

from pathlib import Path


def isFileConfirmed(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False
# end of isFileConfirmed()

def openFastaFile(fastafile: Path) -> dict:
    print(f" openFAstaFile() file is = {fastafile}")