"""
SUBS : Finding a Motif in DNA

Given two strings s and t, t is a substring of s if t is contained as a contiguous 
collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its 
left, including itself (e.g., the positions of all occurrences of 'U' in 
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i 
of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the 
starting and ending positions of the substring in s; for example, if 
s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that 
t will have multiple locations in s if it occurs more than once as a 
substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

"""

from helperFuncs import getMultipleSequences, printListOfInts

def find_motif(s,t,ind=0):
    """
    find_motif(s,t)
    
    Finds occurances of string t within s. Returns list of indexes.
    """
    
    i = s.find(t,ind)
    if i==-1:
        return []
    else:
        return [i+1] + find_motif(s,t,i+2)
    
def test_SUBS():
    s = "GATATATGCATATACTT"
    t = "ATAT"
    locs = [2, 4, 10]
    print(find_motif(s,t))
    assert(find_motif(s,t)==locs)

def main():
    from sys import argv
    s,t = getMultipleSequences(argv[1])
    printListOfInts(find_motif(s,t))

if __name__ == '__main__':
    main()

