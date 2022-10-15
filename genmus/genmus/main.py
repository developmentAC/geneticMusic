#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Program to play DNA input files."""


# from collections import Counter
import sys, random, csv, os
from genmus import player

####

import numpy as np

# from scipy.io import wavfile
import sys, random, os, math

# from Bio import SeqIO #biopython
from itertools import permutations
import itertools


####
# from scipy.io import wavfile

from pathlib import Path 

import typer

from rich.console import Console


from genmus import genmus_helper as gh
from genmus import launcher

import numpy as np

# Run notes:
# virtualenv myenv -p python3
# source myenv/bin/activate
# pip install biopython
# pip install streamlit
# pip install scipy

cli = typer.Typer()

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
        launcher.helper()
        # gh.helper_extended()
        exit()

    if opt.lower() == "s":  # print up some extra help about how to start a virtual env
        names_str = "scale"
        # gh.makeMusicFromChars(names_str, sNotes_list, sDuration_list)
        player.makeMusicFromChars(names_str, player.sNotes_list, player.sDuration_list)
        exit()

    if opt.lower() == "t":  # twinkle, twinkle, little star demo.
        # print(i)
        names_list = [
            "twinkle_star.wav",
            "twinkle_star_left.wav",
            "twinkle_star_right.wav",
        ]
        player.makeMusicDemo(
            names_list,
            player.left_hand_notes,
            player.left_hand_duration,
            player.right_hand_notes,
            player.right_hand_duration,
        )
        exit()
    if file:
        if dir:
            dataFile = dir / file
        else:
            dataFile = file
        print(f"getarguments() :: datafile = {dataFile}")
        print(f" Is this a real file :: {launcher.isFileConfirmed(dataFile)}")
        data = launcher.openFastaFile(dataFile)

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











def pairMusicWordWithNote(this_dic, Twinkle_list):
    """Pair a musical note with a word; most common words to most common notes. this_dic is the freqs of words in a sequence."""

    # print("pairMusicWordWithNote()")

    myMaxValueThisDic_int = max(this_dic.values())
    print(
        "\t Frequencies; ",
        printWithColour(BIGreen, f"{this_dic}"),
        "Max Value :",
        printWithColour(BICyan, f" {myMaxValueThisDic_int}"),
    )
    print("\t Twinkle_list =", printWithColour(BIGreen, f"{Twinkle_list}"))

    # pull all same frequencies values from dic
    freq_dic = {}
    for v in range(myMaxValueThisDic_int):
        # freq_dic[v] = [this_dic[i] == myMaxValueThisDic_int for i in this_dic]
        freq_dic[v] = [
            i for i in this_dic if this_dic[i] == v
        ]  # [i] == myMaxValueThisDic_int for i in this_dic]

    noteParing_dic = {}
    counter = 0

    for i in freq_dic:
        # print(i, freq_dic[i], printWithColour(BICyan, f"{Twinkle_list[counter]}"))
        if len(freq_dic[i]) != 0:
            # notes_dic[Twinkle_list[counter]] = freq_dic[i]
            try:
                # print(f"counter = {counter},{Twinkle_list[counter]} ")
                noteParing_dic[Twinkle_list[counter]] = list(freq_dic[i])
                counter += 1
            except IndexError:
                pass

    # for i in noteParing_dic:
    # 	print(printWithColour(BIBlue,f"{i}"),"::", printWithColour(BIYellow,f"{noteParing_dic[i]}"))
    # print("\n{noteParing_dic}")

    # reverse the notesParing_dic. make: n_dic[note] = "word"
    n_dic = {}
    for i in noteParing_dic:
        tmp_list = noteParing_dic[i]
        for v in tmp_list:
            n_dic[v] = i

    n_dic["n"] = Twinkle_list[-1]  # all other notes that are not in the frequency plan

    return n_dic
    # end of pairMusicWordWithNote()


def sequenceSlidingWindow(seq_str, n_dic):
    """Function to slide over sequence, three bases at a time, to identify words and to create a music score. Inputs: sequence and the word to note conversions."""

    # print(printWithColour(BICyan,"sequenceSlidingWindow()"))

    # print(printWithColour(BIYellow,f"{seq_str}, {n_dic}"))
    # The length of sequence must be divisible by 3. If not, add dummy chars to end

    while len(seq_str) % 3 != 0:
        seq_str = seq_str + "x"
    # print(seq_str)

    playNotes_list = []  # holds the notes to play from seq
    playNotesDuration_list = []  # holds the durations of each note to play from seq
    for i in range(0, len(seq_str), 3):
        word_str = seq_str[i : i + 3]
        note_str = ""
        try:
            note_str = n_dic[word_str]
        except KeyError:
            # print(f"\t [-] Word not found : {word_str}")
            note_str = n_dic["n"]
        playNotes_list.append(note_str)
        playNotesDuration_list.append(0.5)

        # TODO need to give duration in the following way.
        # Twinkle_list =        ["D3", "C3", "E3" , "F3" , "G3" , "A3" , "B2" , "C4"]
        # TwinkleDuration_list = [1.0 , 1.0 , 1.0  , 2    , 1.0  , 2    , 0.5  , 0.5]
        ###########################

    # duration_dic = {}

    # print(f"{playNotes_list} \n {playNotesDuration_list}")

    return playNotes_list, playNotesDuration_list

    # end of slidingWindow()


def getWordCartesianProducts(char_list, wordSize_int):
    """Get a cartenian product of all possible words of length wordSize_int that can be obtained from from the characters in char_list"""

    # print(printWithColour(BIGreen,"getWordCartesianProducts()"))

    words_dic = {}
    tmp_str = ""

    for i in char_list:
        tmp_str = tmp_str + i

    for p in itertools.product(tmp_str, repeat=wordSize_int):
        tmp_str = "".join(p)
        # print(f"\n : {tmp_str}")
        words_dic[tmp_str] = 0
    return words_dic
    # end of getWordCartesianProducts()


def getWordFreq(seq_str, freq_dic):  # string and word
    """get the frequencies of the words a sequence"""

    # print(printWithColour(BICyan,"getWordFreq()"))

    words_list = []
    countsOfWordsInSeqOnly_dic = {}  # record the counts of words for this seq only
    # print(printWithColour(BICyan,f"\t Seq"),"=",printWithColour(BIYellow,f"{seq_str}"))
    for i in freq_dic:
        tmp = seq_str.count(i)
        if tmp > 0:
            # print(printWithColour(BIGreen,f"\t Found: {i} , count = {seq_str.count(i)}"))
            countsOfWordsInSeqOnly_dic[i] = seq_str.count(i)
    return countsOfWordsInSeqOnly_dic


# end of getWordFreq()

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
