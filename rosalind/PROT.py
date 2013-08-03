"""
	PROT:	

"""
from sys import argv
from helperFuncs import getSequence

def rna_transcribe(rna, codonDict):
	i=0
	prot = ''
	while i<len(rna):
		aa = codonDict[rna[i:i+3]]
		if aa=='Stop':
			break
		else:
			prot = prot + aa
		i=i+3
	return prot



rnaCodons = "\
UUU F      CUU L      AUU I      GUU V\n\
UUC F      CUC L      AUC I      GUC V\n\
UUA L      CUA L      AUA I      GUA V\n\
UUG L      CUG L      AUG M      GUG V\n\
UCU S      CCU P      ACU T      GCU A\n\
UCC S      CCC P      ACC T      GCC A\n\
UCA S      CCA P      ACA T      GCA A\n\
UCG S      CCG P      ACG T      GCG A\n\
UAU Y      CAU H      AAU N      GAU D\n\
UAC Y      CAC H      AAC N      GAC D\n\
UAA Stop   CAA Q      AAA K      GAA E\n\
UAG Stop   CAG Q      AAG K      GAG E\n\
UGU C      CGU R      AGU S      GGU G\n\
UGC C      CGC R      AGC S      GGC G\n\
UGA Stop   CGA R      AGA R      GGA G\n\
UGG W      CGG R      AGG R      GGG G"

def makeCodonDict():
	codonDict = {}
	for line in rnaCodons.split('\n'):
		for codon in line.split('   '):
			if len(codon.strip(' ').strip('\n'))>0:
				rna, aa = codon.split(' ')
				codonDict[rna]=aa
	return codonDict


def test_PROT():
	rna="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
	protein = "MAMAPRTEINSTRING"
	codonDict = makeCodonDict()
	prot = rna_transcribe(rna,codonDict)
	print(prot)
	assert(protein==prot)

def main():
	rna = getSequence(argv[1])
	codonDict = makeCodonDict()
	print(rna_transcribe(rna,codonDict))

if __name__=='__main__':
	main()
