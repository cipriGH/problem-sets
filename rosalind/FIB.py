"""
	FIB:    Rabbits and Recurrence Relations
"""
from sys import argv

def rabbit_population(n,k):
    """
        I didn't think I was smart enough to come up with this solution
        on my own. Bam. Recursion.
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return rabbit_population(n-1,k) + k*rabbit_population(n-2,k)

def test_FIB():
    n = 5
    k = 3
    output = 19
    result = rabbit_population(n,k)
    print(result)
    assert(result==output)

def main():
    n,k = argv[1:3]
    print rabbit_population(int(n),int(k))

if __name__=='__main__':
    main()
