"""
    Rosalind Problem 002:	Transcribing DNA into RNA

    

"""
from getSequence import getSequence

def dna_to_rna(dnaseq):
    """
    dna_to_rna(dnaseq)

    Transcribel DNA to RNA
    """
    return dnaseq.replace("T", "U")

def test_RNA():
    sampleDNA = "GCAT"
    sampleOutput = "GCAU"
    assert(dna_to_rna(sampleDNA)==sampleOutput)

def main():
    from sys import argv
    seq = getSequence(argv[1])
    print(dna_to_rna(seq))

if __name__=='__main__':
    main()

