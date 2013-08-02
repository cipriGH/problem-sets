"""
REVC: Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as 
are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by 
reversing the symbols of s, then taking the complement of each symbol 
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.
"""
from helperFuncs import getSequence

def reverse_complement(sequence):
	"""
	reverse_complement(sequence)
	
	Returns the reverse complement of input sequence (string)
	"""
	sequence = sequence.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
	
	return sequence[::-1].upper()

def test_reverse_complement():
	seq = "AAAACCCGGT"
	revcompseq = "ACCGGGTTTT"
	print(reverse_complement(seq))
	assert(reverse_complement(seq)==revcompseq)

def main():
	from sys import argv
	seq = getSequence(argv[1])
	print(reverse_complement(seq))

if __name__=='__main__':
	main()
