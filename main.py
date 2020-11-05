# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# Creating a random DNA sequence for testing
randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])


DNAStr = validateSeq(randDNAStr)
print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFreq(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f'[4] + Reverse compliment: {reverse_compliment(DNAStr)}\n')
print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] + GC Content in subsection k=5: {gc_content_subsec(DNAStr,5)}\n')
print(f'[7] + Aminoacid sequence from DNA: {translate_seq(DNAStr,0)}\n')
print(f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')