# DNA Toolkit file

Nucleotides = ["A", "C", "G", "T"]


# Checking an input sequence whether it is a valid DNA string or not
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


