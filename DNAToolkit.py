# DNA Toolkit file
from structures import *

# Checking an input sequence whether it is a valid DNA string or not
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


# Counting nucleotides
def countNucFreq(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict    

# DNA -> RNA Transcription
def transcription(seq):
    """DNA -> RNA Transcription : Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


# Reverse Complimenting 
def reverse_compliment(seq):
    """ Swaping A with T and G with C and vice versa """
    return ''.join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]