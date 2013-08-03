"""
	IPRB:	Mendel's First Law
	
	
"""
from sys import argv

def possesses_dominant_allele(k,m,n):
    """
    A population has k members who are homozygous dominant, m members 
    heterozygous, and n member homozygous recessive.
    
    This function calculates the probability of a child possessing a dominant
    gene - taking into account all possible parent combinations
    
    Note: The code could be simplified by using some NumPy... 
    TODO: Fix using NumPy
    """
    k = float(k);   m = float(m);   n = float(n);
    tp = k + m + n      #   total population
    
    #	probabilities of passing on dominant allele:
    pkk = 1.0;      pkm = 1.0;      pkn = 1.0
    pmm = 0.75;     pmn = 0.25;     pnn = 0.0
    
    #	probabilities of passing on dominant allele for each mating pair:
    pkk = 1.0;      pkm = 1.0;      pkn = 1.0;
    pmm = 0.75;     pmn = 0.50;     pnn = 0.0;
    
    prob = 0.0
    prob = prob + pkk*(k/tp)*((k-1)/(tp-1))       # k mate with k
    prob = prob + pkm*(k/tp)*((m)/(tp-1))         # k mate with m
    prob = prob + pkm*(m/tp)*((k)/(tp-1))         # m mate with k
    prob = prob + pkn*(k/tp)*((n)/(tp-1))         # k mate with n
    prob = prob + pkn*(n/tp)*((k)/(tp-1))         # n mate with k
    prob = prob + pmm*(m/tp)*((m-1)/(tp-1))       # m mate with m
    prob = prob + pmn*(m/tp)*((n)/(tp-1))         # m mate with n
    prob = prob + pmn*(n/tp)*((m)/(tp-1))         # n mate with m
    prob = prob + pnn*(n/tp)*((n-1)/(tp-1))       # n mate with n
    return prob



def test_IPRB():
    k=2
    m=2
    n=2
    prob=0.78333
    pda=possesses_dominant_allele(k,m,n)
    print(pda)
    assert(abs(pda-prob)<0.00001)


def main():
    k,m,n = argv[1:4]
    print possesses_dominant_allele(k,m,n)

if __name__=='__main__':
    main()
