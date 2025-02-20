# DNA Toolkit file
from structures import *
from collections import Counter

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
    #return ''.join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]

    # Pythonic Approach: FASTER**
    mapping = str.maketrans('ATGC', 'TACG')
    return seq.translate(mapping)[::-1]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    """ GC Content in a DNA/RNA sub-sequence of length k with k = 20 as default value"""
    res = []
    for i in range(0,len(seq)-k+1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res


def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq)-2, 3)]


def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i+3])

    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict         