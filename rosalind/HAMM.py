"""
	HAMM:	Counting Point Mutations

	Given two strings s and t of equal length, the Hamming distance 
	between s and t, denoted dH(s,t), is the number of corresponding 
	symbols that differ in s and t. See Figure 2.

	Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

	Return: The Hamming distance dH(s,t).
"""
from helperFuncs import getMultipleSequences
from sys import argv

def hamming_dist(s,t):
	hd = 0
	for i in range(len(s)):
		if s[i] != t[i]:
			hd = hd + 1
	return hd


def test_hamming_dist():
	s = "GAGCCTACTAACGGGAT"
	t = "CATCGTAATGACGGCCT"
	sampleOutput=7
	assert(hamming_dist(s,t)==sampleOutput)

def main():
	s, t = getMultipleSequences(argv[1])
	print(hamming_dist(s,t))

if __name__=='__main__':
	main()
