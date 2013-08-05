"""
	FIBD:	Mortal Fibonacci Rabbits
	borrowed solution...
"""
from sys import argv

def rabbit_population(n,m=1):
	
	ages = [1] + [0]*(m-1)
	for i in xrange(n-1):
		ages = [sum(ages[1:])] + ages[:-1]
	return sum(ages)
		

def test_FIBD():
	n=6
	m=3
	answer = 4
	
	rp = rabbit_population(n,m)
	print rp
	assert(answer==rp)

def main():
	n,m = argv[1:3]
	n = int(n)
	m = int(m)

	print rabbit_population(n,m)

if __name__=='__main__':
	main()
