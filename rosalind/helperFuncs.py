"""
	getSequence(filename)
	
	Function defined to return a string representation of a nucleotide
	sequence contained with the file at path filename (string)

"""


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
		seqfile = open(filename)
	except IOError:
		print("File could not be opened, or does not exist")
		return
	return seqfile.readline().strip('\n')

def getMultipleSequences(filename=""):
	"""
	"""
	try:
		seqfile = open(filename)
	except IOError:
		print("File could not be opened, or does not exist")
		return
	return [lin.strip('\n') for lin in seqfile.readlines()]

def printListOfInts(listofints):
	print(' '.join([str(c) for c in listofints]))


def getFASTAdict(filename):
	"""
	Reads file containing rosalind's FASTA formatted sequences and 
	returns each id:sequence pair as entries in a python dictionary. 
	"""
	try:
		fastafile = open(filename)
	except IOError:
		print("File could not be opened, or does not exist")
		return
	
	fastalist = ''.join(fastafile.readlines()).replace('\n','').split('>')
	fastalist = [f.strip('>') for f in fastalist]
	
	fastaDict = {}
	
	for p in fastalist:
		fastaDict[p[0:13]]=p[13:]
	
	del fastaDict['']
	#print fastaDict
	
	return fastaDict
