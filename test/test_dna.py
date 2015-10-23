from pycrispr.fasta_sequences import *
from pycrispr.crispr import *
from pycrispr.dna import *

import os
import pytest

test_fasta = "test/test_crispr/GCF_000494755.1_ASM49475v1_genomic.fna"
fasta = FastaSequences(file=test_fasta)

dna = DNA(fasta[0].seq)
dna_size = 9376071

first_string   = "GTGGCCGATACGGTCGACCTTGGCGGGGTGTGGACCGCGGCGACGGACGAGCTGGCGGACGAGATCGCGTCCGCTCAGCA"
similar_string = "GTGGCCGATACGGTCGACCTTGGCGGGGTGTGGACCGCGGCGACGGACGAGCTGGCGGACGAGATCGCGT"
similarity_score = 0.875

def test_seq_length():
    assert dna.seq_length() == dna_size

def test_sub_sequence():
    assert dna.sub_sequence(0, 80) == first_string

def test_sequence_similarity():
    assert DNA.sequence_similarity(first_string, similar_string) == similarity_score
