#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This file contains code to facilitate loading files and running the program. """


DATE = "15 October 2022"
VERSION = "0.1.3"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"


from pathlib import Path

import os, random, sys

THISPROG = sys.argv[0].replace("./", "")
WHATISTHIS_p1 = f"\n\t{THISPROG}: Plays DNA in piano from a FASTA file."
WHATISTHIS_p2 = (
    "\t Use option '-h' for more glorification about this amazing project!\n"
)

MYOUTPUT_DIR = "0_out/"  # all results are saved in this local directory

# PAIRINGFILE = "pairings.txt" # the file containing all information about which gradebook file blongs to what gradebook repository. Note, the names of each the user and the user's gradebook file may not be the same.
# REPOFILE = "dirNames" # file to run the bulk pusher. Contains path and name of each repository to push.


# colour codes

# Bold High Intensity
BIBlack = "\033[1;90m"  # Black
BIRed = "\033[1;91m"  # Red
BIGreen = "\033[1;92m"  # Green
BIYellow = "\033[1;93m"  # Yellow
BIBlue = "\033[1;94m"  # Blue
BIPurple = "\033[1;95m"  # Purple
BICyan = "\033[1;96m"  # Cyan
BIWhite = "\033[1;97m"  # White

# Regular Colors
Black = "\033[0;30m"  # Black
Red = "\033[0;31m"  # Red
Green = "\033[0;32m"  # Green
Yellow = "\033[0;33m"  # Yellow
Blue = "\033[0;34m"  # Blue
Purple = "\033[0;35m"  # Purple
Cyan = "\033[0;36m"  # Cyan
White = "\033[0;37m"  # White

# Bold
BBlack = "\033[1;30m"  # Black
BRed = "\033[1;31m"  # Red
BGreen = "\033[1;32m"  # Green
BYellow = "\033[1;33m"  # Yellow
BBlue = "\033[1;34m"  # Blue
BPurple = "\033[1;35m"  # Purple
BCyan = "\033[1;36m"  # Cyan
BWhite = "\033[1;37m"  # White


# Bold colour list
colour_list = [
    "\033[1;30m",
    "\033[1;31m",
    "\033[1;32m",
    "\033[1;33m",
    "\033[1;34m",
    "\033[1;35m",
    "\033[1;36m",
    "\033[1;37m",
    "\033[1;90m",
    "\033[1;91m",
    "\033[1;92m",
    "\033[1;93m",
    "\033[1;94m",
    "\033[1;95m",
    "\033[1;96m",
    "\033[1;97m",
]


banner1_str = """
\t        ██████╗ ███████╗███╗   ██╗███╗   ███╗██╗   ██╗███████╗       
\t██╗    ██╔════╝ ██╔════╝████╗  ██║████╗ ████║██║   ██║██╔════╝    ██╗
\t╚═╝    ██║  ███╗█████╗  ██╔██╗ ██║██╔████╔██║██║   ██║███████╗    ╚═╝
\t██╗    ██║   ██║██╔══╝  ██║╚██╗██║██║╚██╔╝██║██║   ██║╚════██║    ██╗
\t╚═╝    ╚██████╔╝███████╗██║ ╚████║██║ ╚═╝ ██║╚██████╔╝███████║    ╚═╝
\t        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝       
"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/


def bannerScreen(myCount_int):
    """prints a charming and colourful little message for the user"""
    # report the perceived OS type
    platform_str = get_platformType()

    if platform_str.lower() == "linux" or platform_str.lower() == "osx":
        for i in range(myCount_int):
            randomColour_str = random.choice(
                colour_list
            )  # choose a random colour to display the title screen.
            print(randomColour_str + banner1_str + BIWhite)
    else:
        print(banner1_str)


# end of bannerScreen()


def helper():
    """Cheap and friendly online help; how to use the program"""
    bannerScreen(1)  # print up one banner screen
    print(WHATISTHIS_p1)
    h_str1 = "\t" + DATE + " | version: " + VERSION
    h_str2 = "\t" + AUTHOR + "\n\tmail: " + AUTHORMAIL
    print("\t" + len(h_str2) * "-")
    print(printWithColour(BIYellow, h_str1))
    print("\t" + len(h_str2) * "-")
    print(printWithColour(BIBlue, h_str2))
    # print(h_str2)
    print("\t" + len(h_str2) * "-")
    print("\tOptions:")
    print(
        printWithColour(BIGreen, f"\t [+]"),
        printWithColour(BICyan, f"[--bighelp]"),
        printWithColour(BIYellow, "This page, right?"),
    )
    print(
        printWithColour(BIGreen, f"\t [+]"),
        printWithColour(BICyan, "[--opt S]"),
        printWithColour(BIYellow, "Create a music scale"),
    )
    print(
        printWithColour(BIGreen, f"\t [+]"),
        printWithColour(BICyan, "[--opt T]"),
        printWithColour(BIYellow, "Create song: Twinkle-Twinkle Little Star"),
    )
    print(
        printWithColour(BIGreen, f"\t [+]"),
        printWithColour(BICyan, "[--opt H]"),
        printWithColour(BIYellow, "Create song: Happy Birthday"),
    )
    print(
        printWithColour(BIGreen, f"\t [+]"),
        printWithColour(BICyan, "[--data ./data --file file.fasta]"),
        printWithColour(BIYellow, "Load fasta file, convert dna to score"),
    )
    print(
        printWithColour(BIGreen, f"\t [+]"),
        printWithColour(BICyan, "Setup with Poetry : "),
        printWithColour(BIYellow, "poetry install"),
    )

    print(
        printWithColour(
            BIGreen,
            f"\n\t [+] \U0001f600 USAGE: poetry run {THISPROG} --dir ./data/ --file mydata.fasta ",
        )
    )
    print(printWithColour(BIBlue, "\n\t # --------------------------"))


# end of helper()


def helper_extended():
    """Function to print up extra information for the user."""
    print(printWithColour(BIBlue, "\n\t # --------------------------"))
    print(printWithColour(BIGreen, f"\n\t You are to run {THISPROG} using poetry."))

    # end of helper_extended()


def printWithColour(colCode_str, myMessage_str):
    """A function to print with colour for Unix and MacOS."""
    platform_str = get_platformType()
    if platform_str.lower() == "linux" or platform_str.lower() == "osx":
        myMessage_str = colCode_str + myMessage_str + BIWhite
        # print(colCode_str + myMessage_str + BIWhite)
    else:  # Windows does not seem to like these colourcodes
        # print(myMessage_str)
        pass
    return myMessage_str


# end of printWithColour()


def checkDataDir(dir_str):
    # function to determine whether a data output directory exists.
    # if the directory doesnt exist, then it is created

    try:
        os.makedirs(dir_str)
        # if MYOUTPUT_DIR doesn't exist, create directory
        # printByPlatform("\t Creating :{}".format(dir_str))
        return 1

    except OSError:
        # printErrorByPlatform("\t Error creating directory or directory already present ... ")
        return 0


# end of checkDataDir()


def get_platformType():
    """Function to dermine the OS type."""
    platforms = {
        "darwin": "OSX",
        "win32": "Windows",
        "linux1": "Linux",
        "linux2": "Linux",
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]


# end of get_platformType()


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
