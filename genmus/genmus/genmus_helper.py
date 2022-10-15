#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# from scipy.io import wavfile
import sys, random, os, math

# from Bio import SeqIO #biopython
from itertools import permutations
import itertools

from genmus import player as player

# DATE = "15 October 2022"
# VERSION = "0.1.2"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"

# THISPROG = sys.argv[0].replace("./", "")
# WHATISTHIS_p1 = f"\n\t{THISPROG}: Plays DNA in piano from a FASTA file."
# WHATISTHIS_p2 = (
#     "\t Use option '-h' for more glorification about this amazing project!\n"
# )

# MYOUTPUT_DIR = "0_out/"  # all results are saved in this local directory

# # PAIRINGFILE = "pairings.txt" # the file containing all information about which gradebook file blongs to what gradebook repository. Note, the names of each the user and the user's gradebook file may not be the same.
# # REPOFILE = "dirNames" # file to run the bulk pusher. Contains path and name of each repository to push.


# # colour codes

# # Bold High Intensity
# BIBlack = "\033[1;90m"  # Black
# BIRed = "\033[1;91m"  # Red
# BIGreen = "\033[1;92m"  # Green
# BIYellow = "\033[1;93m"  # Yellow
# BIBlue = "\033[1;94m"  # Blue
# BIPurple = "\033[1;95m"  # Purple
# BICyan = "\033[1;96m"  # Cyan
# BIWhite = "\033[1;97m"  # White

# # Regular Colors
# Black = "\033[0;30m"  # Black
# Red = "\033[0;31m"  # Red
# Green = "\033[0;32m"  # Green
# Yellow = "\033[0;33m"  # Yellow
# Blue = "\033[0;34m"  # Blue
# Purple = "\033[0;35m"  # Purple
# Cyan = "\033[0;36m"  # Cyan
# White = "\033[0;37m"  # White

# # Bold
# BBlack = "\033[1;30m"  # Black
# BRed = "\033[1;31m"  # Red
# BGreen = "\033[1;32m"  # Green
# BYellow = "\033[1;33m"  # Yellow
# BBlue = "\033[1;34m"  # Blue
# BPurple = "\033[1;35m"  # Purple
# BCyan = "\033[1;36m"  # Cyan
# BWhite = "\033[1;37m"  # White


# # Bold colour list
# colour_list = [
#     "\033[1;30m",
#     "\033[1;31m",
#     "\033[1;32m",
#     "\033[1;33m",
#     "\033[1;34m",
#     "\033[1;35m",
#     "\033[1;36m",
#     "\033[1;37m",
#     "\033[1;90m",
#     "\033[1;91m",
#     "\033[1;92m",
#     "\033[1;93m",
#     "\033[1;94m",
#     "\033[1;95m",
#     "\033[1;96m",
#     "\033[1;97m",
# ]


# banner1_str = """
# \t        ██████╗ ███████╗███╗   ██╗███╗   ███╗██╗   ██╗███████╗       
# \t██╗    ██╔════╝ ██╔════╝████╗  ██║████╗ ████║██║   ██║██╔════╝    ██╗
# \t╚═╝    ██║  ███╗█████╗  ██╔██╗ ██║██╔████╔██║██║   ██║███████╗    ╚═╝
# \t██╗    ██║   ██║██╔══╝  ██║╚██╗██║██║╚██╔╝██║██║   ██║╚════██║    ██╗
# \t╚═╝    ╚██████╔╝███████╗██║ ╚████║██║ ╚═╝ ██║╚██████╔╝███████║    ╚═╝
# \t        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝       
# """
# # banner ref: https://manytools.org/hacker-tools/ascii-banner/


# def get_piano_notes():
#     """
#     Get the frequency in hertz for all keys on a standard piano.

#     Returns
#     -------
#     note_freqs : dict :: Mapping between note name and corresponding frequency.

#     """

#     # White keys are in Uppercase and black keys (sharps) are in lowercase
#     octave = ["C", "c", "D", "d", "E", "F", "f", "G", "g", "A", "a", "B"]
#     base_freq = 440  # Frequency of Note A4
#     keys = np.array([x + str(y) for y in range(0, 9) for x in octave])
#     # Trim to standard 88 keys
#     start = np.where(keys == "A0")[0][0]
#     end = np.where(keys == "C8")[0][0]
#     keys = keys[start : end + 1]

#     note_freqs = dict(
#         zip(keys, [2 ** ((n + 1 - 49) / 12) * base_freq for n in range(len(keys))])
#     )
#     note_freqs[""] = 0.0  # stop
#     return note_freqs
#     # end of get_piano_notes()


# def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
#     """
#     Get pure sine wave.

#     Parameters
#     ----------
#     frequency : float 			:: Frequency in hertz.
#     duration : float 			:: Time in seconds.
#     sample_rate : int, optional :: Wav file sample rate. The default is 44100.
#     amplitude : int, optional 	:: Peak Amplitude. The default is 4096.

#     Returns
#     -------
#     wave : TYPE
#         DESCRIPTION.

#     """
#     t = np.linspace(0, duration, int(sample_rate * duration))
#     wave = amplitude * np.sin(2 * np.pi * frequency * t)
#     return wave


# # end of get_sine_wave()


# def apply_overtones(frequency, duration, factor, sample_rate=44100, amplitude=4096):
#     """
#     Return fundamental note with overtones applied.

#     Parameters
#     ----------
#     frequency : float           :: Frequency in hertz.
#     duration : float            :: Time in seconds.
#     factor : list               :: List of floats as fraction of the fundamental amplitude for amplitudes of the overtones.
#     sample_rate : int, optional :: Wav file sample rate. The default is 44100.
#     amplitude : int, optional   :: Peak Amplitude.  The default is 4096.

#     Returns
#     -------
#     fundamental : ndarray :: Output note of `float` type.

#     """
#     assert abs(1 - sum(factor)) < 1e-8

#     frequencies = np.minimum(
#         np.array([frequency * (x + 1) for x in range(len(factor))]), sample_rate // 2
#     )
#     amplitudes = np.array([amplitude * x for x in factor])

#     fundamental = get_sine_wave(frequencies[0], duration, sample_rate, amplitudes[0])
#     for i in range(1, len(factor)):
#         overtone = get_sine_wave(frequencies[i], duration, sample_rate, amplitudes[i])
#         fundamental += overtone
#     return fundamental


# # end of apply_overtones()


# def get_adsr_weights(
#     frequency, duration, length, decay, sustain_level, sample_rate=44100
# ):
#     """
#     ADSR(attack, decay, sustain, and release) envelop generator with exponential
#     weights applied.

#     Parameters
#     ----------
#     frequency : float           :: Frequency in hertz.
#     duration : float            ::  Time in seconds.
#     length : list               ::  List of fractions that indicates length of each stage in ADSR.
#     decay : list                :: List of float for decay factor to be used in each stage for exponential weights.
#     sustain_level : float       :: Amplitude of `S` stage as a fraction of max amplitude.
#     sample_rate : int, optional :: Wav file sample rate. The default is 44100.

#     Returns
#     -------
#     weights : ndarray

#     """
#     try:
#         from scipy.io import wavfile
#     except ModuleNotFoundError:
#         print(
#             printWithColour(
#                 BIRed,
#                 f"\t [+] The sciPy library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
#             )
#         )
#         exit()

#     assert abs(sum(length) - 1) < 1e-8
#     assert len(length) == len(decay) == 4

#     intervals = int(duration * frequency)
#     len_A = np.maximum(int(intervals * length[0]), 1)
#     len_D = np.maximum(int(intervals * length[1]), 1)
#     len_S = np.maximum(int(intervals * length[2]), 1)
#     len_R = np.maximum(int(intervals * length[3]), 1)

#     decay_A = decay[0]
#     decay_D = decay[1]
#     decay_S = decay[2]
#     decay_R = decay[3]

#     A = 1 / np.array([(1 - decay_A) ** n for n in range(len_A)])
#     A = A / np.nanmax(A)
#     D = np.array([(1 - decay_D) ** n for n in range(len_D)])
#     D = D * (1 - sustain_level) + sustain_level
#     S = np.array([(1 - decay_S) ** n for n in range(len_S)])
#     S = S * sustain_level
#     R = np.array([(1 - decay_R) ** n for n in range(len_R)])
#     R = R * S[-1]

#     weights = np.concatenate((A, D, S, R))
#     smoothing = np.array([0.1 * (1 - 0.1) ** n for n in range(5)])
#     smoothing = smoothing / np.nansum(smoothing)
#     weights = np.convolve(weights, smoothing, mode="same")

#     weights = np.repeat(weights, int(sample_rate * duration / intervals))
#     tail = int(sample_rate * duration - weights.shape[0])
#     if tail > 0:
#         weights = np.concatenate(
#             (weights, weights[-1] - weights[-1] / tail * np.arange(tail))
#         )
#     return weights


# # end of get_adsr_weights()


# def apply_pedal(note_values, bar_value):
#     """
#     Press and hold the sustain pedal throughout the bar.

#     Parameters
#     ----------
#     note_values : list :: List of note duration.
#     bar_value : float  :: Duration of a measure in seconds.

#     Returns
#     -------
#     new_values : list :: List of note duration with sustain.

#     """

#     # print("apply_pedal()")
#     print(printWithColour(BIBlue, f"\t[+] Initial bar_value = {bar_value}"))
#     print(printWithColour(BIBlue, f"\t[+] sum(note_values) = {sum(note_values)}"))
#     # print(printWithColour(BIRed,f" note_values = {note_values}"))

#     if (
#         sum(note_values) % bar_value != 0
#     ):  # This seems to fix a bug; both vars must be equal.
#         # diff_flt = (sum(note_values) % bar_value) # remove this amount to get an even division
#         # print(printWithColour(BIRed,f"\t [+] Discrepancy, diff_flt = {diff_flt} from note_values type(note_values) = {type(note_values)}\n{note_values}."))
#         # note_values.append(diff_flt)
#         # note_values[len(note_values)-1] = 1#note_values[len(note_values)-1] + diff_flt

#         # find a bar_value that divides sum(note_values)
#         counter = sum(note_values) % bar_value
#         while sum(note_values) % counter != 0:
#             counter = round(
#                 counter + 0.1, 2
#             )  # round to two decimal places to avoid long trails of random error
#             # print(f"counter = {counter}, sum(note_values) = {sum(note_values)}")
#         bar_value = counter

#     print(printWithColour(BIBlue, f"\t[+] Reset bar_value = {bar_value}"))
#     # print(printWithColour(BIGreen,f"\t[+] sum(note_values) = {sum(note_values)}"))

#     assert sum(note_values) % bar_value == 0

#     new_values = []
#     start = 0
#     while True:
#         cum_value = np.cumsum(np.array(note_values[start:]))
#         end = np.where(cum_value == bar_value)[0][0]
#         if end == 0:
#             new_values += [note_values[start]]
#         else:
#             this_bar = np.array(note_values[start : start + end + 1])
#             new_values += [
#                 bar_value - np.sum(this_bar[:i]) for i in range(len(this_bar))
#             ]
#         start += end + 1
#         if start == len(note_values):
#             break
#     return new_values
#     # end of apply_pedal()


# def get_song_data(
#     music_notes,
#     note_values,
#     bar_value,
#     factor,
#     length,
#     decay,
#     sustain_level,
#     sample_rate=44100,
#     amplitude=4096,
# ):
#     """
#     Generate song from notes.

#     Parameters
#     ----------
#     music_notes : list :: List of note names.
#     note_values : list :: List of note duration.
#     bar_value: float   :: Duration of a bar.
#     factor : list      :: Factor to be used to generate overtones.
#     length : list      :: Stage length to be used to calculate ADSR weights.
#     decay : list       :: Stage decay to be used to calculate ADSR weights.
#     sustain_level : float :: Amplitude of `S` stage as a fraction of max amplitude.
#     sample_rate : int, optional :: Wav file sample rate. The default is 44100.
#     amplitude : int, optional :: Peak Amplitude. The default is 4096.

#     Returns
#     -------
#     song : ndarray

#     """
#     note_freqs = get_piano_notes()
#     frequencies = [note_freqs[note] for note in music_notes]
#     new_values = apply_pedal(note_values, bar_value)
#     duration = int(sum(note_values) * sample_rate)
#     end_idx = np.cumsum(np.array(note_values) * sample_rate).astype(int)
#     start_idx = np.concatenate(([0], end_idx[:-1]))
#     end_idx = np.array(
#         [start_idx[i] + new_values[i] * sample_rate for i in range(len(new_values))]
#     ).astype(int)

#     song = np.zeros((duration,))
#     for i in range(len(music_notes)):
#         this_note = apply_overtones(frequencies[i], new_values[i], factor)
#         weights = get_adsr_weights(
#             frequencies[i], new_values[i], length, decay, sustain_level
#         )
#         song[start_idx[i] : end_idx[i]] += this_note * weights

#     song = song * (amplitude / np.max(song))
#     return song


# # end of get_song_data()


# def checkDataDir(dir_str):
#     # function to determine whether a data output directory exists.
#     # if the directory doesnt exist, then it is created

#     try:
#         os.makedirs(dir_str)
#         # if MYOUTPUT_DIR doesn't exist, create directory
#         # printByPlatform("\t Creating :{}".format(dir_str))
#         return 1

#     except OSError:
#         # printErrorByPlatform("\t Error creating directory or directory already present ... ")
#         return 0


# # end of checkDataDir()


# def get_platformType():
#     """Function to dermine the OS type."""
#     platforms = {
#         "darwin": "OSX",
#         "win32": "Windows",
#         "linux1": "Linux",
#         "linux2": "Linux",
#     }
#     if sys.platform not in platforms:
#         return sys.platform
#     return platforms[sys.platform]


# # end of get_platformType()


# def printWithColour(colCode_str, myMessage_str):
#     """A function to print with colour for Unix and MacOS."""
#     platform_str = get_platformType()
#     if platform_str.lower() == "linux" or platform_str.lower() == "osx":
#         myMessage_str = colCode_str + myMessage_str + BIWhite
#         # print(colCode_str + myMessage_str + BIWhite)
#     else:  # Windows does not seem to like these colourcodes
#         # print(myMessage_str)
#         pass
#     return myMessage_str


# # end of printWithColour()


# def bannerScreen(myCount_int):
#     """prints a charming and colourful little message for the user"""
#     # report the perceived OS type
#     platform_str = get_platformType()

#     if platform_str.lower() == "linux" or platform_str.lower() == "osx":
#         for i in range(myCount_int):
#             randomColour_str = random.choice(
#                 colour_list
#             )  # choose a random colour to display the title screen.
#             print(randomColour_str + banner1_str + BIWhite)
#     else:
#         print(banner1_str)


# # end of bannerScreen()


# def helper():
#     """Cheap and friendly online help; how to use the program"""
#     bannerScreen(1)  # print up one banner screen
#     print(WHATISTHIS_p1)
#     h_str1 = "\t" + DATE + " | version: " + VERSION
#     h_str2 = "\t" + AUTHOR + "\n\tmail: " + AUTHORMAIL
#     print("\t" + len(h_str2) * "-")
#     print(printWithColour(BIYellow, h_str1))
#     print("\t" + len(h_str2) * "-")
#     print(printWithColour(BIBlue, h_str2))
#     # print(h_str2)
#     print("\t" + len(h_str2) * "-")
#     print("\tOptions:")
#     print(
#         printWithColour(BIGreen, f"\t [+]"),
#         printWithColour(BICyan, f"[--bighelp]"),
#         printWithColour(BIYellow, "This page, right?"),
#     )
#     print(
#         printWithColour(BIGreen, f"\t [+]"),
#         printWithColour(BICyan, "[--opt S]"),
#         printWithColour(BIYellow, "Create a music scale"),
#     )
#     print(
#         printWithColour(BIGreen, f"\t [+]"),
#         printWithColour(BICyan, "[--opt T]"),
#         printWithColour(BIYellow, "Create song: Twinkle-Twinkle Little Star"),
#     )
#     print(
#         printWithColour(BIGreen, f"\t [+]"),
#         printWithColour(BICyan, "[--opt E]"),
#         printWithColour(
#             BIYellow, "Instructions for running this wonderous tool.\n\t\t"
#         ),
#     )
#     # print(printWithColour(BIGreen,f"\n\t[+] \U0001f600 USAGE: ./{THISPROG}  dnaFile.fasta"))
#     print(
#         printWithColour(BICyan, "\t [+] Setup with Poetry : "),
#         printWithColour(BIYellow, "poetry install"),
#     )

#     print(
#         printWithColour(
#             BIGreen,
#             f"\n\t [+] \U0001f600 USAGE: poetry run {THISPROG}  --data ./data/dnaFile.fasta",
#         )
#     )
#     print(printWithColour(BIBlue, "\n\t # --------------------------"))


# # end of helper()


# def helper_extended():
#     """Function to print up extra information for the user."""
#     print(printWithColour(BIBlue, "\n\t # --------------------------"))
#     print(printWithColour(BIGreen, f"\n\t You are to run {THISPROG} using poetry."))

#     # print(printWithColour(BIGreen,"\n\t # Running the container"))
#     # print(printWithColour(BICyan,"\t Linux:"), printWithColour(BIYellow,"sh dockerRunScripts/run_linux.sh"))
#     # print(printWithColour(BICyan,"\t MacOS:"), printWithColour(BIYellow,"sh dockerRunScripts/run_macOS.sh"))
#     # print(printWithColour(BICyan,"\t Windows:"), printWithColour(BIYellow,"dockerRunScripts\\run_win.bat"))

#     # Check what has been installed.
#     # python3 -m pip freeze > requirements.txt

#     # end of helper_extended()


# def openDnaSeq(fastaFile_str):
#     """open a fasta file, return the dna sequences"""

#     # print(printWithColour(BIGreen, "openDnaSeq()"))
#     try:
#         from Bio import SeqIO  # biopython
#     except ModuleNotFoundError:
#         print(
#             printWithColour(
#                 BIRed,
#                 f"\t [+] The BioPython library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
#             )
#         )
#         exit()

#     print(printWithColour(BIYellow, f"\t [+] Opening FASTA file {fastaFile_str}\n"))
#     seq_dic = {}
#     for record in SeqIO.parse(fastaFile_str, "fasta"):
#         seq_dic[(str(record.id))] = str(record.seq).upper()
#         # print(record.seq, type(record.seq) )
#     if len(seq_dic) == 0:
#         print(
#             printWithColour(
#                 BIRed, f"\t [+] Bad format or incorrect Fasta file: <<{fastaFile_str}>>"
#             )
#         )
#         exit()
#     print(printWithColour(BIYellow, f"\t Listed Sequences :"))
#     # for i in seq_dic:
#     # 	print(printWithColour(BIGreen, f"\t [+] "), printWithColour(BIYellow, f"{i}"),":",printWithColour(BICyan, f"{seq_dic[i]}"))

#     return seq_dic
#     # end of openDnaSeq()


# def pairMusicWordWithNote(this_dic, Twinkle_list):
#     """Pair a musical note with a word; most common words to most common notes. this_dic is the freqs of words in a sequence."""

#     # print("pairMusicWordWithNote()")

#     myMaxValueThisDic_int = max(this_dic.values())
#     print(
#         "\t Frequencies; ",
#         printWithColour(BIGreen, f"{this_dic}"),
#         "Max Value :",
#         printWithColour(BICyan, f" {myMaxValueThisDic_int}"),
#     )
#     print("\t Twinkle_list =", printWithColour(BIGreen, f"{Twinkle_list}"))

#     # pull all same frequencies values from dic
#     freq_dic = {}
#     for v in range(myMaxValueThisDic_int):
#         # freq_dic[v] = [this_dic[i] == myMaxValueThisDic_int for i in this_dic]
#         freq_dic[v] = [
#             i for i in this_dic if this_dic[i] == v
#         ]  # [i] == myMaxValueThisDic_int for i in this_dic]

#     noteParing_dic = {}
#     counter = 0

#     for i in freq_dic:
#         # print(i, freq_dic[i], printWithColour(BICyan, f"{Twinkle_list[counter]}"))
#         if len(freq_dic[i]) != 0:
#             # notes_dic[Twinkle_list[counter]] = freq_dic[i]
#             try:
#                 # print(f"counter = {counter},{Twinkle_list[counter]} ")
#                 noteParing_dic[Twinkle_list[counter]] = list(freq_dic[i])
#                 counter += 1
#             except IndexError:
#                 pass

#     # for i in noteParing_dic:
#     # 	print(printWithColour(BIBlue,f"{i}"),"::", printWithColour(BIYellow,f"{noteParing_dic[i]}"))
#     # print("\n{noteParing_dic}")

#     # reverse the notesParing_dic. make: n_dic[note] = "word"
#     n_dic = {}
#     for i in noteParing_dic:
#         tmp_list = noteParing_dic[i]
#         for v in tmp_list:
#             n_dic[v] = i

#     n_dic["n"] = Twinkle_list[-1]  # all other notes that are not in the frequency plan

#     return n_dic
#     # end of pairMusicWordWithNote()


# def sequenceSlidingWindow(seq_str, n_dic):
#     """Function to slide over sequence, three bases at a time, to identify words and to create a music score. Inputs: sequence and the word to note conversions."""

#     # print(printWithColour(BICyan,"sequenceSlidingWindow()"))

#     # print(printWithColour(BIYellow,f"{seq_str}, {n_dic}"))
#     # The length of sequence must be divisible by 3. If not, add dummy chars to end

#     while len(seq_str) % 3 != 0:
#         seq_str = seq_str + "x"
#     # print(seq_str)

#     playNotes_list = []  # holds the notes to play from seq
#     playNotesDuration_list = []  # holds the durations of each note to play from seq
#     for i in range(0, len(seq_str), 3):
#         word_str = seq_str[i : i + 3]
#         note_str = ""
#         try:
#             note_str = n_dic[word_str]
#         except KeyError:
#             # print(f"\t [-] Word not found : {word_str}")
#             note_str = n_dic["n"]
#         playNotes_list.append(note_str)
#         playNotesDuration_list.append(0.5)

#         # TODO need to give duration in the following way.
#         # Twinkle_list =        ["D3", "C3", "E3" , "F3" , "G3" , "A3" , "B2" , "C4"]
#         # TwinkleDuration_list = [1.0 , 1.0 , 1.0  , 2    , 1.0  , 2    , 0.5  , 0.5]
#         ###########################

#     # duration_dic = {}

#     # print(f"{playNotes_list} \n {playNotesDuration_list}")

#     return playNotes_list, playNotesDuration_list

#     # end of slidingWindow()


# def getWordCartesianProducts(char_list, wordSize_int):
#     """Get a cartenian product of all possible words of length wordSize_int that can be obtained from from the characters in char_list"""

#     # print(printWithColour(BIGreen,"getWordCartesianProducts()"))

#     words_dic = {}
#     tmp_str = ""

#     for i in char_list:
#         tmp_str = tmp_str + i

#     for p in itertools.product(tmp_str, repeat=wordSize_int):
#         tmp_str = "".join(p)
#         # print(f"\n : {tmp_str}")
#         words_dic[tmp_str] = 0
#     return words_dic
#     # end of getWordCartesianProducts()


# def getWordFreq(seq_str, freq_dic):  # string and word
#     """get the frequencies of the words a sequence"""

#     # print(printWithColour(BICyan,"getWordFreq()"))

#     words_list = []
#     countsOfWordsInSeqOnly_dic = {}  # record the counts of words for this seq only
#     # print(printWithColour(BICyan,f"\t Seq"),"=",printWithColour(BIYellow,f"{seq_str}"))
#     for i in freq_dic:
#         tmp = seq_str.count(i)
#         if tmp > 0:
#             # print(printWithColour(BIGreen,f"\t Found: {i} , count = {seq_str.count(i)}"))
#             countsOfWordsInSeqOnly_dic[i] = seq_str.count(i)
#     return countsOfWordsInSeqOnly_dic


# # end of getWordFreq()


# def makeNotesFromSeq():
#     """determine a conversion of dna to notes for playing"""
#     print("makeNotesFromSeq()")
#     notes_list = []
#     perm = permutations(["A", "T", "C", "G"], 2)
#     for i in list(perm):
#         # print (i)
#         notes_list.append(i)
#     print(notes_list)
#     dnaNotes_dic = {}  # create a dictionary of base pairs to notes


# def makeMusicDemo(
#     names_list,
#     left_hand_notes,
#     left_hand_duration,
#     right_hand_notes=[],
#     right_hand_duration=[],
# ):

#     try:
#         from scipy.io import wavfile
#     except ModuleNotFoundError:
#         print(
#             printWithColour(
#                 BIRed,
#                 f"\t [+] The sciPy library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
#             )
#         )
#         exit()

#     factor = [0.68, 0.26, 0.03, 0.0, 0.03]
#     length = [0.01, 0.6, 0.29, 0.1]
#     decay = [0.05, 0.02, 0.005, 0.1]
#     sustain_level = 0.1
#     right_hand = get_song_data(
#         right_hand_notes, right_hand_duration, 2, factor, length, decay, sustain_level
#     )

#     factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01, 0.01]
#     length = [0.01, 0.29, 0.6, 0.1]
#     decay = [0.05, 0.02, 0.005, 0.1]
#     left_hand = get_song_data(
#         left_hand_notes, left_hand_duration, 2, factor, length, decay, sustain_level
#     )

#     data = left_hand + right_hand
#     data_l = left_hand
#     data_r = right_hand

#     data = data * (4096 / np.max(data))
#     data_l = data_l * (4096 / np.max(data_l))
#     data_r = data_r * (4096 / np.max(data_r))

#     checkDataDir(MYOUTPUT_DIR)
#     wavfile.write(MYOUTPUT_DIR + names_list[0], 44100, data.astype(np.int16))
#     wavfile.write(MYOUTPUT_DIR + names_list[1], 44100, data_l.astype(np.int16))
#     wavfile.write(MYOUTPUT_DIR + names_list[2], 44100, data_r.astype(np.int16))


# # end of makeMusicDemo()


# def makeMusicFromChars(name_str : str, notes_list: list, duration_list: list):
#     """Function to convert chars to musical wav file."""
#     try:
#         from scipy.io import wavfile
#     except ModuleNotFoundError:
#         print(
#             printWithColour(
#                 BIRed,
#                 f"\t [+] The sciPy library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
#             )
#         )
#         exit()
#     # print("makeMusicFromChars()")

#     factor = [0.68, 0.26, 0.03, 0.0, 0.03]
#     length = [0.01, 0.6, 0.29, 0.1]
#     decay = [0.05, 0.02, 0.005, 0.1]
#     sustain_level = 0.1
#     data = player.get_song_data(
#         notes_list, duration_list, 2, factor, length, decay, sustain_level
#     )
#     # print(printWithColour(BIRed,f"\t[+] data = {data}"))

#     # factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01  , 0.01]
#     # length = [0.01, 0.29, 0.6, 0.1]
#     # decay = [0.05,0.02,0.005,0.1]
#     # left_hand = get_song_data(left_hand_notes, left_hand_duration, 2, factor, length, decay, sustain_level)

#     # data = left_hand + right_hand
#     # data_l = left_hand
#     # data_r = right_hand

#     data = data * (4096 / np.max(data))
#     # data_l = data_l * (4096/np.max(data_l))
#     # data_r = data_r * (4096/np.max(data_r))
#     #
#     checkDataDir(MYOUTPUT_DIR)
#     name_str = name_str + ".wav"
#     filename = MYOUTPUT_DIR + name_str
#     wavfile.write(MYOUTPUT_DIR + name_str, 44100, data.astype(np.int16))
#     print(printWithColour(BICyan, f"\t[+] Saving <{filename}>\n" + White))

# # end of makeMusicFromChars()
