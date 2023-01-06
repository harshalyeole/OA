import itertools

def oddpair(N):
    L = itertools.permutations(N, 2)
    print(list(L))
    

N = [2,6,1,8,4,9,0,8]
oddpair(N)
# commentt