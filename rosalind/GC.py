"""
	GC: Computing GC Content
	
	The GC-content of a DNA string is given by the percentage of symbols
	in the string that are 'C' or 'G'. For example, the GC-content of 
	"AGCTATAG" is 37.5%. Note that the reverse complement of any DNA 
	string has the same GC-content.

	DNA strings must be labeled when they are consolidated into a 
	database. A commonly used method of string labeling is called FASTA 
	format. In this format, the string is introduced by a line that 
	begins with '>', followed by some labeling information. Subsequent 
	lines contain the string itself; the first line to begin with '>' 
	indicates the label of the next string.

	In Rosalind's implementation, a string in FASTA format will be 
	labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit
	code between 0000 and 9999.

	Given: At most 10 DNA strings in FASTA format (of length at most 
	1 kbp each).

	Return: The ID of the string having the highest GC-content, followed
	by the GC-content of that string. Rosalind allows for a default 
	error of 0.001 in all decimal answers unless otherwise stated; 
	please see the note on absolute error below.
"""
from sys import argv
from helperFuncs import getFASTAdict

def compute_gc_content(seq):
	"""
	returns gc content
	"""
	return 100.0*(seq.count('C') + seq.count('G'))/len(seq)

def find_max_gc_content_in_fastadict(fastadict):
	"""
	
	"""
	returnstr = ""
	maxcontent = 0.0
	for key in fastadict:
		gc = compute_gc_content(fastadict[key])
		if gc>maxcontent:
			maxcontent=gc
			returnstr = key + '\n' + str(gc)
	return returnstr

def test_gc():
	fastadict = {'Rosalind_0808': 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT',
	'Rosalind_5959': 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
	'Rosalind_6404': 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'}
	maxgc = "Rosalind_0808\n60.91954"
	print find_max_gc_content_in_fastadict(fastadict)
	assert(find_max_gc_content_in_fastadict(fastadict)[0:len(maxgc)]==maxgc)


def main():
	fastadict = getFASTAdict(argv[1])
	print(find_max_gc_content_in_fastadict(fastadict))


if __name__=='__main__':
	main()





