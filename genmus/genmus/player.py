#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains information about playing notes. """

# Utility functions for writing music in Python.
# Some music playing code was borrowed from the below open source project
# Ref: https://github.com/katieshiqihe/music_in_python/blob/main/twinkle.py
# Ref: https://towardsdatascience.com/music-in-python-2f054deb41f4

import numpy as np
from genmus import launcher
import os

# from playsound import playsound # does not seem to work with poetry add playsound...


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

# # happybirthday
# HB_list = [
# "C3","C3","C3","D3","C3","F3","E3","C3","C3","D3","C3","G3","F3","C3","C3","C3","A3","F3","E3","D3","B4","B4","A3","F3","G3","F3"]

# happybirthday
HB_list = [
    "C3",
    "C3",
    "D3",
    "C3",
    "F3",
    "E3",
    "C3",
    "C3",
    "D3",
    "C3",
    "G3",
    "F3",
    "C3",
    "C3",
    "A3",
    "F3",
    "E3",
    "D3",
    "B3",
    "B3",
    "A3",
    "F3",
    "G3",
    "F3",
]
# old     # "C3","C3","C3","D3","C3","F3","E3","C3","C3","D3","C3","G3","F3","C3","C3","C3","A3","F3","E3","D3","B4","B4","A3","F3","G3","F3"]


HB_sd_list = [
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


def get_piano_notes():
    """
    Get the frequency in hertz for all keys on a standard piano.

    Returns
    -------
    note_freqs : dict :: Mapping between note name and corresponding frequency.

    """

    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ["C", "c", "D", "d", "E", "F", "f", "G", "g", "A", "a", "B"]
    base_freq = 440  # Frequency of Note A4
    keys = np.array([x + str(y) for y in range(0, 9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == "A0")[0][0]
    end = np.where(keys == "C8")[0][0]
    keys = keys[start : end + 1]

    note_freqs = dict(
        zip(keys, [2 ** ((n + 1 - 49) / 12) * base_freq for n in range(len(keys))])
    )
    note_freqs[""] = 0.0  # stop
    return note_freqs
    # end of get_piano_notes()


def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    """
    Get pure sine wave.

    Parameters
    ----------
    frequency : float 			:: Frequency in hertz.
    duration : float 			:: Time in seconds.
    sample_rate : int, optional :: Wav file sample rate. The default is 44100.
    amplitude : int, optional 	:: Peak Amplitude. The default is 4096.

    Returns
    -------
    wave : TYPE
        DESCRIPTION.

    """
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave


# end of get_sine_wave()


def apply_overtones(frequency, duration, factor, sample_rate=44100, amplitude=4096):
    """
    Return fundamental note with overtones applied.

    Parameters
    ----------
    frequency : float           :: Frequency in hertz.
    duration : float            :: Time in seconds.
    factor : list               :: List of floats as fraction of the fundamental amplitude for amplitudes of the overtones.
    sample_rate : int, optional :: Wav file sample rate. The default is 44100.
    amplitude : int, optional   :: Peak Amplitude.  The default is 4096.

    Returns
    -------
    fundamental : ndarray :: Output note of `float` type.

    """
    assert abs(1 - sum(factor)) < 1e-8

    frequencies = np.minimum(
        np.array([frequency * (x + 1) for x in range(len(factor))]), sample_rate // 2
    )
    amplitudes = np.array([amplitude * x for x in factor])

    fundamental = get_sine_wave(frequencies[0], duration, sample_rate, amplitudes[0])
    for i in range(1, len(factor)):
        overtone = get_sine_wave(frequencies[i], duration, sample_rate, amplitudes[i])
        fundamental += overtone
    return fundamental


# end of apply_overtones()


def get_adsr_weights(
    frequency, duration, length, decay, sustain_level, sample_rate=44100
):
    """
    ADSR(attack, decay, sustain, and release) envelop generator with exponential
    weights applied.

    Parameters
    ----------
    frequency : float           :: Frequency in hertz.
    duration : float            ::  Time in seconds.
    length : list               ::  List of fractions that indicates length of each stage in ADSR.
    decay : list                :: List of float for decay factor to be used in each stage for exponential weights.
    sustain_level : float       :: Amplitude of `S` stage as a fraction of max amplitude.
    sample_rate : int, optional :: Wav file sample rate. The default is 44100.

    Returns
    -------
    weights : ndarray

    """
    try:
        from scipy.io import wavfile
    except ModuleNotFoundError:
        print(
            launcher.printWithColour(
                BIRed,
                f"\t [+] The sciPy library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
            )
        )
        exit()

    assert abs(sum(length) - 1) < 1e-8
    assert len(length) == len(decay) == 4

    intervals = int(duration * frequency)
    len_A = np.maximum(int(intervals * length[0]), 1)
    len_D = np.maximum(int(intervals * length[1]), 1)
    len_S = np.maximum(int(intervals * length[2]), 1)
    len_R = np.maximum(int(intervals * length[3]), 1)

    decay_A = decay[0]
    decay_D = decay[1]
    decay_S = decay[2]
    decay_R = decay[3]

    A = 1 / np.array([(1 - decay_A) ** n for n in range(len_A)])
    A = A / np.nanmax(A)
    D = np.array([(1 - decay_D) ** n for n in range(len_D)])
    D = D * (1 - sustain_level) + sustain_level
    S = np.array([(1 - decay_S) ** n for n in range(len_S)])
    S = S * sustain_level
    R = np.array([(1 - decay_R) ** n for n in range(len_R)])
    R = R * S[-1]

    weights = np.concatenate((A, D, S, R))
    smoothing = np.array([0.1 * (1 - 0.1) ** n for n in range(5)])
    smoothing = smoothing / np.nansum(smoothing)
    weights = np.convolve(weights, smoothing, mode="same")

    weights = np.repeat(weights, int(sample_rate * duration / intervals))
    tail = int(sample_rate * duration - weights.shape[0])
    if tail > 0:
        weights = np.concatenate(
            (weights, weights[-1] - weights[-1] / tail * np.arange(tail))
        )
    return weights


# end of get_adsr_weights()


def apply_pedal(note_values, bar_value):
    """
    Press and hold the sustain pedal throughout the bar.

    Parameters
    ----------
    note_values : list :: List of note duration.
    bar_value : float  :: Duration of a measure in seconds.

    Returns
    -------
    new_values : list :: List of note duration with sustain.

    """

    # print("apply_pedal()")

    # print(
    #     launcher.printWithColour(
    #         launcher.BIBlue, f"\t [+] Initial bar_value = {bar_value}"
    #     )
    # )
    # print(
    #     launcher.printWithColour(
    #         launcher.BIBlue, f"\t [+] sum(note_values) = {sum(note_values)}"
    #     )
    # )

    # print(launcher.printWithColour(launcher.BIRed,f" note_values = {note_values}"))

    if (
        sum(note_values) % bar_value != 0
    ):  # This seems to fix a bug; both vars must be equal.
        # diff_flt = (sum(note_values) % bar_value) # remove this amount to get an even division
        # print(launcher.printWithColour(launcher.BIRed,f"\t [+] Discrepancy, diff_flt = {diff_flt} from note_values type(note_values) = {type(note_values)}\n{note_values}."))
        # note_values.append(diff_flt)
        # note_values[len(note_values)-1] = 1#note_values[len(note_values)-1] + diff_flt

        # find a bar_value that divides sum(note_values)
        counter = sum(note_values) % bar_value
        while sum(note_values) % counter != 0:
            counter = round(
                counter + 0.1, 2
            )  # round to two decimal places to avoid long trails of random error
            # print(f"counter = {counter}, sum(note_values) = {sum(note_values)}")
        bar_value = counter

    # print(
    #     launcher.printWithColour(
    #         launcher.BIBlue, f"\t [+] Reset bar_value = {bar_value}"
    #     )
    # )

    # print(launcher.printWithColour(launcher.BIGreen,f"\t [+] sum(note_values) = {sum(note_values)}"))

    assert sum(note_values) % bar_value == 0

    new_values = []
    start = 0
    while True:
        cum_value = np.cumsum(np.array(note_values[start:]))
        end = np.where(cum_value == bar_value)[0][0]
        if end == 0:
            new_values += [note_values[start]]
        else:
            this_bar = np.array(note_values[start : start + end + 1])
            new_values += [
                bar_value - np.sum(this_bar[:i]) for i in range(len(this_bar))
            ]
        start += end + 1
        if start == len(note_values):
            break
    return new_values
    # end of apply_pedal()


def get_song_data(
    music_notes,
    note_values,
    bar_value,
    factor,
    length,
    decay,
    sustain_level,
    sample_rate=44100,
    amplitude=4096,
):
    """
    Generate song from notes.

    Parameters
    ----------
    music_notes : list :: List of note names.
    note_values : list :: List of note duration.
    bar_value: float   :: Duration of a bar.
    factor : list      :: Factor to be used to generate overtones.
    length : list      :: Stage length to be used to calculate ADSR weights.
    decay : list       :: Stage decay to be used to calculate ADSR weights.
    sustain_level : float :: Amplitude of `S` stage as a fraction of max amplitude.
    sample_rate : int, optional :: Wav file sample rate. The default is 44100.
    amplitude : int, optional :: Peak Amplitude. The default is 4096.

    Returns
    -------
    song : ndarray

    """
    note_freqs = get_piano_notes()
    frequencies = [note_freqs[note] for note in music_notes]
    new_values = apply_pedal(note_values, bar_value)
    duration = int(sum(note_values) * sample_rate)
    end_idx = np.cumsum(np.array(note_values) * sample_rate).astype(int)
    start_idx = np.concatenate(([0], end_idx[:-1]))
    end_idx = np.array(
        [start_idx[i] + new_values[i] * sample_rate for i in range(len(new_values))]
    ).astype(int)

    song = np.zeros((duration,))
    for i in range(len(music_notes)):
        this_note = apply_overtones(frequencies[i], new_values[i], factor)
        weights = get_adsr_weights(
            frequencies[i], new_values[i], length, decay, sustain_level
        )
        song[start_idx[i] : end_idx[i]] += this_note * weights

    song = song * (amplitude / np.max(song))
    return song


# end of get_song_data()


def makeNotesFromSeq():
    """determine a conversion of dna to notes for playing"""
    print("makeNotesFromSeq()")
    notes_list = []
    perm = permutations(["A", "T", "C", "G"], 2)
    for i in list(perm):
        # print (i)
        notes_list.append(i)
    print(notes_list)
    dnaNotes_dic = {}  # create a dictionary of base pairs to notes


def makeMusicDemo(
    names_list,
    left_hand_notes,
    left_hand_duration,
    right_hand_notes=[],
    right_hand_duration=[],
):
    print("\t Playing a demo ...")
    try:
        from scipy.io import wavfile
    except ModuleNotFoundError:
        print(
            launcher.printWithColour(
                launcher.BIRed,
                f"\t [+] The sciPy library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
            )
        )
        exit()

    factor = [0.68, 0.26, 0.03, 0.0, 0.03]
    length = [0.01, 0.6, 0.29, 0.1]
    decay = [0.05, 0.02, 0.005, 0.1]
    sustain_level = 0.1
    right_hand = get_song_data(
        right_hand_notes, right_hand_duration, 2, factor, length, decay, sustain_level
    )

    factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01, 0.01]
    length = [0.01, 0.29, 0.6, 0.1]
    decay = [0.05, 0.02, 0.005, 0.1]
    left_hand = get_song_data(
        left_hand_notes, left_hand_duration, 2, factor, length, decay, sustain_level
    )

    data = left_hand + right_hand
    data_l = left_hand
    data_r = right_hand

    data = data * (4096 / np.max(data))
    data_l = data_l * (4096 / np.max(data_l))
    data_r = data_r * (4096 / np.max(data_r))

    launcher.checkDataDir(launcher.MYOUTPUT_DIR)
    wavfile.write(launcher.MYOUTPUT_DIR + names_list[0], 44100, data.astype(np.int16))
    wavfile.write(launcher.MYOUTPUT_DIR + names_list[1], 44100, data_l.astype(np.int16))
    wavfile.write(launcher.MYOUTPUT_DIR + names_list[2], 44100, data_r.astype(np.int16))
    filename = launcher.MYOUTPUT_DIR + names_list[2]
    playSound(filename)


# end of makeMusicDemo()


def makeMusicFromChars(name_str: str, notes_list: list, duration_list: list):
    """Function to convert chars to musical wav file."""
    try:
        from scipy.io import wavfile
    except ModuleNotFoundError:
        print(
            launcher.printWithColour(
                launcher.BIRed,
                f"\t [+] The sciPy library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
            )
        )
        # exit()
    # print("makeMusicFromChars()")

    factor = [0.68, 0.26, 0.03, 0.0, 0.03]
    length = [0.01, 0.6, 0.29, 0.1]
    decay = [0.05, 0.02, 0.005, 0.1]
    sustain_level = 0.1
    data = get_song_data(
        notes_list, duration_list, 2, factor, length, decay, sustain_level
    )

    data = data * (4096 / np.max(data))

    launcher.checkDataDir(launcher.MYOUTPUT_DIR)
    name_str = name_str + ".wav"
    filename = launcher.MYOUTPUT_DIR + name_str
    wavfile.write(filename, 44100, data.astype(np.int16))
    print(
        launcher.printWithColour(
            launcher.BICyan, f"\t[+] Saving <{filename}>\n" + launcher.White
        )
    )
    playSound(filename)


# end of makeMusicFromChars()


def playSound(fname_str: str) -> None:
    """plays the outputted wav file"""
    print(
        launcher.BIGreen + f"\t [+] PLAYING Music file :{fname_str}" + launcher.BIWhite
    )
    platform_str = launcher.get_platformType()
    if platform_str.lower() == "linux":
        myMessage_str = (
            launcher.BIYellow
            + "\t [+] Playing music using aplay on Linux"
            + launcher.BIWhite
        )
        print(myMessage_str)
        os.system(f"aplay {fname_str}")  # this may only work on linux machines...
    if platform_str.lower() == "osx":
        myMessage_str = (
            launcher.BIYellow
            + "\t [+] Playing music using afplay on MacOS"
            + launcher.BIWhite
        )
        print(myMessage_str)
        os.system(f"afplay {fname_str}")  # this may only work on linux machines...
