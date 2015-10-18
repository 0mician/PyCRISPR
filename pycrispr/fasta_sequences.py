class FastaSequences:

    class Fasta:
        def __init__(self, header, seq):
            self.header = header
            self.seq = seq
        
        def __str__(self):
            return "Header: %s\nSequence: %s\n" % (self.header, self.seq)

    def __init__(self, file=None, string=None):
        self.fasta = []
        if(file):
            self.__set_content_from_file(file)
        if(string):
            self.__set_content_from_string(string)

    def __iter__(self):
        i = 0
        size = len(self.fasta)
        while(i < size):
            yield self.fasta[i]
            i += 1

    def is_empty(self):
        return len(self.fasta) == 0

    def __validate_fasta(self, fasta):
        if(not fasta):
            raise ValueError

    def __read_file(self, file):
        fasta_file = open(file, 'r')
        content = fasta_file.readlines()
        return content

    def __set_content_from_file(self, file):
        content = self.__read_file(file)
        self.__set_content(content)

    def __set_content_from_string(self, string):
        content = string.split("\n")
        self.__validate_fasta(content)
        self.__get_content(content)

    def __set_content(self, content):
        self.__validate_fasta(content)
        size = len(content)
        i = 0
        while(i < size):
            sequence = header = ""
            if(content[i].startswith(">")):
                header = content[i][1:].strip("\n") # header, stripped of >
                i += 1
                while(i < size and not content[i].startswith(">")):
                    sequence += content[i].strip("\n")
                    i += 1
            self.fasta.append(FastaSequences.Fasta(header, sequence))
    
