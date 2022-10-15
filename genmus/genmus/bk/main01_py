#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Program to play DNA input files."""


# from collections import Counter
import sys, random, csv, os

# from scipy.io import wavfile

from pathlib import Path

import typer

from rich.console import Console

cli = typer.Typer()


from genmus import genmus_helper as gh
import numpy as np

# Run notes:
# virtualenv myenv -p python3
# source myenv/bin/activate
# pip install biopython
# pip install streamlit
# pip install scipy


###########################
right_hand_notes = [
    "C4",
    "C4",
    "G4",
    "G4",
    "A4",
    "A4",
    "G4",
    "F4",
    "F4",
    "E4",
    "E4",
    "D4",
    "D4",
    "C4",
    "G4",
    "G4",
    "F4",
    "F4",
    "E4",
    "E4",
    "D4",
    "G4",
    "G4",
    "F4",
    "F4",
    "E4",
    "E4",
    "D4",
    "C4",
    "C4",
    "G4",
    "G4",
    "A4",
    "A4",
    "G4",
    "F4",
    "F4",
    "E4",
    "E4",
    "D4",
    "D4",
    "C4",
]


right_hand_duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1] * 6

# Twinkle-Twinkle Little Star
left_hand_notes = [
    "C3",
    "A3",
    "F3",
    "D3",
    "C3",
    "G3",
    "F3",
    "E3",
    "D3",
    "G3",
    "F3",
    "E3",
    "D3",
    "C3",
    "E3",
    "G3",
    "C4",
    "A3",
    "A3",
    "G3",
    "F3",
    "B2",
    "E3",
    "C3",
    "D3",
    "D3",
    "C3",
]

# Twinkle-Twinkle frequency Mapping
# D3	5
# C3	4
# E3	4
# F3	4
# G3	4
# A3	3
# B2	1
# C4	1


left_hand_duration = [
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    1,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    1,
]

###########################
# Twinkle_list: most common to least common notes
# TwinkleDuration_list: corresponding durations of most common to least common notes
Twinkle_list = ["D3", "C3", "E3", "F3", "G3", "A3", "B2", "C4"]
TwinkleDuration_list = [1.0, 1.0, 1.0, 2, 1.0, 2, 0.5, 0.5]
###########################


sNotes_list = [
    "C1",
    "C2",
    "C3",
    "C4",
    "D1",
    "D2",
    "D3",
    "D4",
    "E1",
    "E2",
    "E3",
    "E4",
    "G1",
    "G2",
    "G3",
    "G4",
    "F1",
    "F2",
    "F3",
    "F4",
    "A1",
    "A2",
    "A3",
    "A4",
    "B1",
    "B2",
    "B3",
    "B4",
]

sDuration_list = [
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
]

###########################


s_list = [
    "G3",
    "D3",
    "G3",
    "F3",
    "C3",
    "C4",
    "F3",
    "F3",
    "C3",
    "F3",
    "F3",
    "F3",
    "C3",
    "D3",
    "E3",
    "C3",
    "D3",
    "F3",
    "F3",
    "F3",
    "C3",
    "G3",
    "D3",
    "F3",
    "C3",
    "F3",
    "F3",
    "F3",
    "C3",
    "C3",
    "C3",
    "C3",
    "D3",
    "F3",
    "F3",
    "F3",
    "C3",
    "F3",
    "F3",
    "F3",
    "C3",
    "F3",
    "F3",
    "D3",
    "D3",
    "C3",
    "E3",
    "D3",
    "G3",
    "F3",
    "C3",
    "C4",
    "F3",
    "F3",
    "C3",
    "F3",
    "F3",
    "F3",
    "C3",
    "D3",
    "E3",
    "C3",
    "D3",
    "F3",
    "F3",
    "F3",
    "C3",
    "G3",
    "D3",
    "F3",
    "C3",
    "F3",
    "F3",
    "F3",
    "C3",
    "C3",
    "C3",
    "C3",
    "D3",
    "F3",
    "F3",
    "F3",
    "C3",
    "F3",
    "F3",
    "F3",
    "C3",
    "F3",
    "F3",
    "D3",
    "D3",
    "C3",
    "C4",
]


sd_list = [
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    1,
]

###########################


@cli.command()


# def getArguments(argv_list):
def getArguments2(bighelp: bool = False, opt: str = ""):
    """New get arguments function"""

    if bighelp == True:  # print up some extra help about how to start a virtual env
        gh.helper()
        # gh.helper_extended()
        exit()

    if opt.lower() == "s":  # print up some extra help about how to start a virtual env
        names_str = "scale"
        # gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
        gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
        exit()

    if opt.lower() == "t":  # twinkle, twinkle, little star demo.
        # print(i)
        names_list = [
            "twinkle_star.wav",
            "twinkle_star_left.wav",
            "twinkle_star_right.wav",
        ]
        gh.makeMusicDemo(
            names_list,
            left_hand_notes,
            left_hand_duration,
            right_hand_notes,
            right_hand_duration,
        )
        exit()


# end of getArguments2()


def oldAetArguments(argv_list):
    """A function to determine what parameters have been entered and then completed tasks"""

    # print(argv_list)

    param_1 = "FASTA"  # call for begin() with filename
    param_2 = "-H"  # call for helper()
    param_3 = "-T"  # call for a demo
    param_4 = "-S"  # call for a scale demo
    param_5 = "-E"  # print up extra help

    if len(argv_list) == 0:
        # Output welcome message
        # print(printWithColour(BICyan,gh.WHATISTHIS_p1))
        print(gh.printWithColour(gh.BICyan, gh.WHATISTHIS_p2))

    helperFlag_Bool = False
    fastaFile_str = None  # file to open
    for i in argv_list:
        # print(BIRed + f"Checking <<{i}>>" + White)
        if param_1 in i.upper():
            print(i)
            fastaFile_str = i
            # print(f"\t CSV file found: {myfile_str}")
        if param_2 == i.upper():
            # print(f"\t Call to help found: {i}")
            helperFlag_Bool = True
            gh.helper()
            exit()

        if (
            param_3 in i.upper()
        ):  # automatically push all gradebook files into their corresponding repositories
            # print(i)
            names_list = [
                "twinkle_star.wav",
                "twinkle_star_left.wav",
                "twinkle_star_right.wav",
            ]
            gh.makeMusicDemo(
                names_list,
                left_hand_notes,
                left_hand_duration,
                right_hand_notes,
                right_hand_duration,
            )
            exit()

        if (
            param_4 in i.upper()
        ):  # automatically push all gradebook files into their corresponding repositories
            # print(i)
            names_str = "scale"
            # gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
            gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
            exit()

        if (
            param_5 in i.upper()
        ):  # print up some extra help about how to start a virtual env
            gh.helper()
            gh.helper_extended()
            exit()

        if (
            param_1 not in i.upper()
            and param_2 not in i.upper()
            and param_3 not in i.upper()
            and param_4 not in i.upper()
            and param_5 not in i.upper()
        ):
            print(gh.printWithColour(gh.BICyan, gh.WHATISTHIS_p2))
            exit()

        if fastaFile_str != None:
            begin(fastaFile_str)
            exit()
    # end of oldGetArguments()


def begin(fastaFile_str):
    """Driver function"""
    print(gh.printWithColour(gh.BIYellow, f"\t [+] File to open: {fastaFile_str}\n"))
    seq_dic = gh.openDnaSeq(fastaFile_str)
    freq_dic = gh.getWordCartesianProducts(
        ["A", "T", "C", "G"], 3
    )  # get the permutations of length 3 of ATGC words
    # print(gh.printWithColour(gh.BIYellow,f"\n\t Frequencies of words from Freq_dic :\n\t {freq_dic},\n\t Number of words: {len(freq_dic)}"))

    print(gh.printWithColour(gh.BIGreen, f"Preparing words..."))
    # need to assign most common piano notes to most common words.
    for i in seq_dic:
        # for i in freq_dic:
        print(f"begin(): seq is {i}")
        # print(gh.printWithColour(gh.BIBlue,f"\t {i}"),":", gh.printWithColour(gh.BIGreen,f"{seq_dic[i]}"))
        this_dic = gh.getWordFreq(
            seq_dic[i], freq_dic
        )  # get the word counts from this seq.

        # noteParing_dic = gh.pairMusicWordWithNote(this_dic, Twinkle_list) # Pair the highest word frequencies with most common piano notes
        noteParing_dic = gh.pairMusicWordWithNote(
            this_dic, sNotes_list
        )  # Pair the highest word frequencies with most common piano notes
        scaleNotes_list, scaleDuration_list = gh.sequenceSlidingWindow(
            seq_dic[i], noteParing_dic
        )  # slide through the sequence, read words, then prepare a list of notes to play.
        gh.makeMusicFromChars(i, scaleNotes_list, scaleDuration_list)
        # gh.makeMusicFromChars(i, s_list, sd_list)


# end of begin()


if __name__ == "__main__":
    getArguments2(sys.argv[1:])
