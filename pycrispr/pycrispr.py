import argparse
import os

def valid_file(parser, arg):
    path = os.path.abspath(arg)
    if(not os.path.exists(arg)):
       parser.error("The file %s does not exist" % arg)
    else:
       return arg

parser = argparse.ArgumentParser(description='Tool to discover CRISPR regions in prokaryote genomes')

parser.add_argument('--minNR', dest='minNR', type=int, default=3, help='minimum number of repeats a CRISPR array must contain')
parser.add_argument('--minRL', dest='minRL', type=int, default=19, help='minimum length of the repeat')
parser.add_argument('--maxRL', dest='maxRL', type=int, default=38, help='maximum length of the repeat')
parser.add_argument('--minSL', dest='minSL', type=int, default=19, help='minimum length of the spacer')
parser.add_argument('--maxSL', dest='maxSL', type=int, default=48, help='maximum length of the spacer')
parser.add_argument('--window-length', dest='window_length', type=int, default=8, choices=xrange(6,10), help='length of the search window used to discover CRISPRs')
parser.add_argument('--in', dest='input_file', type=lambda x: valid_file(parser, x), help='input (fasta file)')

args = parser.parse_args()

if __name__ == '__main__':
    minNR = args.minNR
    print(minNR)
