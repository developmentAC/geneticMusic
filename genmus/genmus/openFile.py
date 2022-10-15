#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genmus import launcher

""" This file contains code to facilitate loading files and running the program. """


def openFastaFile(fastaFile_str: str) -> dict:
    """open a fasta file, return the dna sequences"""

    # print(printWithColour(BIGreen, "openDnaSeq()"))
    try:
        from Bio import SeqIO  # biopython
    except ModuleNotFoundError:
        print(
            launcher.printWithColour(
                launcher.BIRed,
                f"\t [+] The BioPython library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
            )
        )
        exit()

    print(
        launcher.printWithColour(
            launcher.BIYellow, f"\t [+] Opening FASTA file {fastaFile_str}\n"
        )
    )
    seq_dic = {}
    for record in SeqIO.parse(fastaFile_str, "fasta"):
        seq_dic[(str(record.id))] = str(record.seq).upper()
        # print(record.seq, type(record.seq) )
    if len(seq_dic) == 0:
        print(
            launcher.printWithColour(
                launcher.BIRed, f"\t [+] Bad format or incorrect Fasta file: <<{fastaFile_str}>>"
            )
        )
        exit()
    print(launcher.printWithColour(launcher.BIYellow, f"\t Listed Sequences :"))

    return seq_dic
    # end of openFastaFile()
