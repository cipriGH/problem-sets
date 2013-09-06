"""
    Rosalind Problem    -   Enumerating Gene Orders

    Given: A positive integer n.

    Return: The total number of permutations of length n, followed by a list of 
    all such permutations (in any order).

"""
import sys

def enum(n):
    # brute force
    count = 0
    enumlist = []
    for i in xrange(1,n+1):
        for j in xrange(i+1,n+1):
            for k in xrange(j+1,n+1):
                count+=1
                enumlist.append((i,j,k))
    return count, enumlist



def test_enum():
    nEnum, listOfEnum = enum(3);
    assert(nEnum==6)

if __name__=='__main__':
    nEnum, listOfEnum = enum(int(sys.argv[1]))
    print nEnum
    for i,j,k in listOfEnum:
        print i, j, k
