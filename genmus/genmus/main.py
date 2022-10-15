#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Program to play DNA input files."""


# from collections import Counter
import sys, random, csv, os
from genmus import player as player
from genmus import launcher as launcher


# from scipy.io import wavfile

from pathlib import Path # TODO look for file exists code

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


@cli.command()

# def getArguments(argv_list):
# def getArguments(bighelp: bool = False, opt: str = "", dataFile: str = ""):

def getArguments(
    bighelp: bool = False,
    opt: str = "",
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
) -> str:
    """New get arguments function"""

    if bighelp == True:  # print up some extra help about how to start a virtual env
        gh.helper()
        # gh.helper_extended()
        exit()

    if opt.lower() == "s":  # print up some extra help about how to start a virtual env
        names_str = "scale"
        # gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
        gh.makeMusicFromChars(names_str, player.sNotes_list, player.sDuration_list)
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
            player.left_hand_notes,
            player.left_hand_duration,
            player.right_hand_notes,
            player.right_hand_duration,
        )
        exit()
    if dataFile.lower:
        dataFile = dir / dataFile
        print(f"data file == {dataFile}")
        launcher.isFileConfirmed(dataFile)


# end of getArguments()


# def oldAetArguments(argv_list):
#     """A function to determine what parameters have been entered and then completed tasks"""

#     # print(argv_list)

#     param_1 = "FASTA"  # call for begin() with filename
#     param_2 = "-H"  # call for helper()
#     param_3 = "-T"  # call for a demo
#     param_4 = "-S"  # call for a scale demo
#     param_5 = "-E"  # print up extra help

#     if len(argv_list) == 0:
#         # Output welcome message
#         # print(printWithColour(BICyan,gh.WHATISTHIS_p1))
#         print(gh.printWithColour(gh.BICyan, gh.WHATISTHIS_p2))

#     helperFlag_Bool = False
#     fastaFile_str = None  # file to open
#     for i in argv_list:
#         # print(BIRed + f"Checking <<{i}>>" + White)
#         if param_1 in i.upper():
#             print(i)
#             fastaFile_str = i
#             # print(f"\t CSV file found: {myfile_str}")
#         if param_2 == i.upper():
#             # print(f"\t Call to help found: {i}")
#             helperFlag_Bool = True
#             gh.helper()
#             exit()

#         if (
#             param_3 in i.upper()
#         ):  # automatically push all gradebook files into their corresponding repositories
#             # print(i)
#             names_list = [
#                 "twinkle_star.wav",
#                 "twinkle_star_left.wav",
#                 "twinkle_star_right.wav",
#             ]
#             gh.makeMusicDemo(
#                 names_list,
#                 left_hand_notes,
#                 left_hand_duration,
#                 right_hand_notes,
#                 right_hand_duration,
#             )
#             exit()

#         if (
#             param_4 in i.upper()
#         ):  # automatically push all gradebook files into their corresponding repositories
#             # print(i)
#             names_str = "scale"
#             # gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
#             gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
#             exit()

#         if (
#             param_5 in i.upper()
#         ):  # print up some extra help about how to start a virtual env
#             gh.helper()
#             gh.helper_extended()
#             exit()

#         if (
#             param_1 not in i.upper()
#             and param_2 not in i.upper()
#             and param_3 not in i.upper()
#             and param_4 not in i.upper()
#             and param_5 not in i.upper()
#         ):
#             print(gh.printWithColour(gh.BICyan, gh.WHATISTHIS_p2))
#             exit()

#         if fastaFile_str != None:
#             begin(fastaFile_str)
#             exit()
#     # end of oldGetArguments()


def begin(fastaFile_str):
    """Driver function"""
    # print(gh.printWithColour(gh.BIYellow, f"\t [+] File to open: {fastaFile_str}\n"))
    # seq_dic = gh.openDnaSeq(fastaFile_str)
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
    getArguments(sys.argv[1:])
