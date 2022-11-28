# Python 3 Program for the above approach
 
# Function to find the count of integers
# such that A[i]%A[j] = 0 or A[j]%A[i] = 0
# for each index of the array A[]

def countIndex(A, N):
    MAX = max(A)
    freq = [0 for i in range(MAX+1)]
    for i in range(N):
        if A[i] in freq:
            freq[A[i]] += 1
        else:
            freq[A[i]] = 1
    res = [0 for i in range(MAX+1)]
    for i in range(1, MAX + 1, 1):
        for j in range(i, MAX + 1, i):
            if (i == j):
                res[i] += (freq[j] - 1)
            else:
                res[i] += freq[j]
                res[j] += freq[i]
    for i in range(N):
        print(res[A[i]],end = " ")
 
# Driver Code

if __name__ == '__main__':

    A = [5,5,2,4,3,7]

    N = len(A)
 

    # Function Call

    countIndex(A, N)

     

    # This code is contributed by SURENDRA_GANGWAR.