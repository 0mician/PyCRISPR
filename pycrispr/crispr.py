class Crispr:
    def __init__(self, dna, repeats=[], repeat_length=0):
        self.dna = dna
        self.repeats = repeats
        self.repeat_length = repeat_length

    def start_array(self):
        return self.repeats[0]

    def end_array(self):
        return self.repeats[-1] + self.repeat_length

    def get_repeat_at(self, pos):
        start = self.repeats[pos] - 1
        return self.dna.seq[start:start+self.repeat_length]
    
    def get_spacer_at(self, pos):
        start = self.repeats[pos] + self.repeat_length - 1
        end = self.repeats[pos+1] - 1
        return self.dna.seq[start:end]

    def add_repeat(self, val):
        self.repeat.append(val)

    def remove_repeat(self, val):
        self.repeat.remove(val)

    def number_of_spacers(self):
        return len(self.repeats) - 1;

    def number_of_repeats(self):
        return len(self.repeats)

    def avg_spacer_length(self):
        return self.repeat_length

    def first_repeat(self):
        return self.repeats[0]

    def last_repeat(self):
        return self.repeats[-1]
        
    def repeat_at(self, pos):
        return self.repeats[pos]

    def repeat_spacing(self, pos1, pos2):
        return abs(repeat_at[pos2] - repeat_at[pos1])

    def insert_repeat_at(self, val, pos):
        self.repeats.insert(pos, val)

    def set_repeat_at(self, val, pos):
        self.repeats[pos] = val
