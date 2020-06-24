# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# Creating a random DNA sequence for testing
randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(20)])


DNAStr = validateSeq(randDNAStr)

print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFreq(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f'[4] + Reverse compliment: {reverse_compliment(DNAStr)}\n')