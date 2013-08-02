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
		file = open(filename)
	except IOError:
		print("File could not be opened, or does not exist")
		return
	return file.readline().strip('\n')

def getMultipleSequences(filename=""):
	"""
	"""
	try:
		file = open(filename)
	except IOError:
		print("File could not be opened, or does not exist")
		return
	return [lin.strip('\n') for lin in file.readlines()]

def printListOfInts(listofints):
	print(' '.join([str(c) for c in listofints]))
