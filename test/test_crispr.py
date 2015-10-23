from pycrispr.fasta_sequences import *
from pycrispr.crispr import *
from pycrispr.dna import *

import os
import pytest

test_fasta = "test/test_crispr/GCF_000494755.1_ASM49475v1_genomic.fna"
fasta = FastaSequences(file=test_fasta)

dna = DNA(fasta.fasta[0].seq)
repeats = [ 456959, 457004, 457050, 457096, 457141, 457187, 457235 ]
repeat_length = 25

crispr_test = Crispr(dna, repeats, repeat_length)

repeat_string = [ "CCCGGTTGGGAGCGTTTACTAACTC",
                  "CCGGTTAGTGAGCGTTTACCAACTC",
                  "CCGGTTAGTGAGCGTTTACCAACGC",
                  "TCGGTTAGTGAGCGTTTACCAACCC",
                  "CCGGTTGGTGAGCGTTTACTAACCC",
                  "CCGGTTGGTGAGCGTTTACTAACCC",
                  "CCGGTTGGTGAGCGTTTACTAACCC" ]

spacer_string = [ "CAGCGGGTGGCTGGGCGCCG",
                  "CGCTGGGCTGGCTGGACGCCG",
                  "CGCTGGGCTGGCTGGACGCGC",
                  "GAACAGGGTGGTCGGCGTCC",
                  "GGGCCGAGCGATCGCGCGTCT",
                  "CTGGGTCGGGCGGCTGTGCGCCC" ]

def test_number_of_spacers():
    assert crispr_test.number_of_spacers() == 6

def test_number_of_repeats():
    assert crispr_test.number_of_repeats() == 7

def test_get_repeat_at():
    i = 0
    for repeat in repeat_string:
        assert crispr_test.get_repeat_at(i) == repeat
        i += 1

def test_get_spacer_at():
    i = 0
    for spacer in spacer_string:
        assert crispr_test.get_spacer_at(i) == spacer
        i += 1

