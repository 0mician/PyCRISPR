from Levenshtein import *

class DNA:
    def __init__(self, seq):
        self.seq = seq

    @staticmethod
    def sequence_similarity(seq1, seq2):
        max_length = max(len(seq1), len(seq2))
        similarity = 1.0 - distance(seq1, seq2) / max_length
        return similarity

    def sub_sequence(self, begin, end):
        return self.seq[begin:end]

    def seq_length(self):
        return len(self.seq)
