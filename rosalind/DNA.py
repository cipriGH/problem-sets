"""
	Rosalind Problem 001:	Counting DNA Nucleotides
	
	Given: A DNA string s of length at most 1000 nt.

	Return: Four integers (separated by spaces) counting the respective 
	number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
	
"""
def count_nucleotides(sequence):
	"""
	count_nucleotides(sequence)
	
	Counts number of A, C, G, and T nucleotides in a DNA sequence.
	
	Parameters
	----------
	sequence : string
			   String containing DNA sequence
	
	Returns
	-------
	nucCounts : list of int
			 List object containing the 4 counts of A, C, G, and T
			 nucleotides.
	"""
	nA = sequence.count('A')
	nC = sequence.count('C')
	nG = sequence.count('G')
	nT = sequence.count('T')
	nucCounts = (nA, nC, nG, nT)
	return nucCounts

def getSequence(filename=""):
	"""
	getSequence(filename)
	
	Reads nucleotide sequence from a single-line file
	
	Parameters
	----------
	filename : string
			   String passed from command line containing path to file
	
	Returns
	-------
	sequence : string
			   String containing nucleotide sequence.
	
	"""
	try:
		file = open(filename)
	except IOError:
		print("File could not be opened, or does not exist")
		return
	return file.readline().strip('\n')

def printListOfInts(listofints):
	print(' '.join([str(c) for c in listofints]))
	
def test_DNA():
	sampleDNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATT" + \
	"AAAAAAAGAGTGTCTGATAGCAGC"
	sampleOutput = (20, 12, 17, 21)	# nA, nC, nG, nT

	assert(count_nucleotides(sampleDNA)==sampleOutput)

if __name__=='__main__':
	from sys import argv
	seq = getSequence(argv[1])
	printListOfInts(count_nucleotides(seq))
