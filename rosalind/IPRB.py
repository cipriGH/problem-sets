"""
	IPRB:	Mendel's First Law
	
	
"""
from sys import argv

def possesses_dominant_allele(k,m,n):
	tp = float(k + m + n)	#	total pop
	#	probabilities of passing on dominant allele:
	pk = 1.0;   pm = 0.5;   pn = 0.0
	
	prob = 0.0
	
	prob = prob + pk*pk*(k/tp)*((k-1)/(tp-1))       # k mate with k
	prob = prob + pk*pm*(k/tp)*((m)/(tp-1))			# k mate with m
	prob = prob + pk*pn*(k/tp)*((n)/(tp-1))			# k mate with n
	prob = prob + pm*pm*(m/tp)*((m-1)/(tp-1))		# m mate with m
	prob = prob + pm*pn*(m/tp)*((n)/(tp-1))			# m mate with n
	prob = prob + pn*pn*(n/tp)*((n-1)/(tp-1))		# n mate with n
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
