#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Program to play DNA input files."""

# from collections import Counter
from genmus import openFile, player, launcher

import numpy as np

# from scipy.io import wavfile
import itertools, sys, random, os

# from Bio import SeqIO #biopython
from itertools import permutations

# from scipy.io import wavfile

from pathlib import Path

import typer

from rich.console import Console

cli = typer.Typer()

@cli.command()
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

    if opt.lower() == "s":  # play scalerint up some extra help about how to start a virtual env
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

    if opt.lower() == "h":  # play happy birthday
        names_str = "happy_birthday"
        player.makeMusicFromChars(names_str, player.HB_list, player.HB_sd_list)
        exit()

    if file:
        if dir:
            dataFile = dir / file
        else:
            dataFile = file
        print(f"getarguments() :: datafile = {dataFile}")
        print(f" Is this a real file :: {launcher.isFileConfirmed(dataFile)}")
        seq_dic = openFile.openFastaFile(dataFile)
        # print(f"getArgruments()  File opened :{data}")
        baseLimit_int = 50 # determine how much of the sequnce to print to screen.
        for i in seq_dic:
            print(
                launcher.printWithColour(launcher.BIGreen, f"\t [+=+] "),
                launcher.printWithColour(launcher.BIYellow, f"{i}"),
                ":",
                launcher.printWithColour(launcher.BICyan, f"{seq_dic[i][:baseLimit_int]}"),
            )
            if len(seq_dic[i]) > baseLimit_int: print(f"(\t Note: printing sequence to {baseLimit_int} bases)")

        begin(seq_dic)


# end of getArguments()


def pairMusicWordWithNote(this_dic, Twinkle_list):
    """ Pair a musical note with a word; most common words to most common notes. this_dic is the freqs of words in a sequence."""

    # print("pairMusicWordWithNote()")

    myMaxValueThisDic_int = max(this_dic.values())
    print(
        launcher.printWithColour(launcher.BIYellow,"\t [+] Frequencies; "),
        launcher.printWithColour(launcher.BIGreen, f"{this_dic}"),
        "Max Value :",
        launcher.printWithColour(launcher.BICyan, f" {myMaxValueThisDic_int}"),
    )
    print("\t Twinkle_list =", launcher.printWithColour(launcher.BIGreen, f"{Twinkle_list}"))

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
    """ Function to slide over sequence, three bases at a time, to identify words and to create a music score. Inputs: sequence and the word to note conversions."""

    print(launcher.printWithColour(launcher.BICyan,"\t [+] sequenceSlidingWindow()"))
    print(launcher.printWithColour(launcher.BIYellow,f" {n_dic}"))
    # The length of sequence must be divisible by 3. If not, add dummy chars to end

    while len(seq_str) % 3 != 0:
        seq_str = seq_str + "x"
    # print(seq_str)

    playNotes_list = []  # holds the notes to play from seq
    playNotesDuration_list = []  # holds the durations of each note to play from seq
    for i in range(0, len(seq_str), 3):
        word_str = seq_str[i : i + 3]
        # print(f" sequenceSlidingWindow() :: {word_str}, note: {n_dic[word_Str]}")
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


def begin(seq_dic: dict) -> None:
    """Driver function"""
    # print(gh.printWithColour(gh.BIYellow, f"\t [+] File to open: {fastaFile_str}\n"))
    # seq_dic = gh.openDnaSeq(fastaFile_str)
    freq_dic = getWordCartesianProducts(
        ["A", "T", "C", "G"], 3
    )  # get the permutations of length 3 of ATGC words
    # print(launcher.printWithColour(launcher.BIYellow,f"\n\t Frequencies of words from Freq_dic :\n\t {freq_dic},\n\t Number of words: {len(freq_dic)}"))
    # print(f"freq_dic : {freq_dic}")

    # print(launcher.printWithColour(launcher.BIGreen, f"Preparing words..."))

    # need to assign most common piano notes to most common words.
    for i in seq_dic:
        # for i in freq_dic:
        print(launcher.printWithColour(launcher.BICyan,f"\t [+] begin() seq is {i}"))
        # print(launcher.printWithColour(launcher.BIBlue,f"\t {i}"),":", launcher.printWithColour(launcher.BIGreen,f"{seq_dic[i]}"))
        this_dic = getWordFreq(
            seq_dic[i], freq_dic
        )  # get the word counts from this seq.

        # noteParing_dic = launcher.pairMusicWordWithNote(this_dic, Twinkle_list) # Pair the highest word frequencies with most common piano notes
        noteParing_dic = pairMusicWordWithNote(
            this_dic, player.sNotes_list
        )  # Pair the highest word frequencies with most common piano notes
        scaleNotes_list, scaleDuration_list = sequenceSlidingWindow(
            seq_dic[i], noteParing_dic
        )  # slide through the sequence, read words, then prepare a list of notes to play.
        player.makeMusicFromChars(i, scaleNotes_list, scaleDuration_list)
        # gh.makeMusicFromChars(i, s_list, sd_list)


# end of begin()


if __name__ == "__main__":
    getArguments(sys.argv[1:])
