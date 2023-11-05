NUM_OF_BLOCKS = 1024

def TwoPivotBlockQuicksort(A, l = None, r = None):
    if l is None:
        l, r = 0, len(A)-1
        
    if l < r:
        i, j = TwoPivotBlockPartition(A, l, r)
        TwoPivotBlockQuicksort(A, l, i-1)
        TwoPivotBlockQuicksort(A, i+1, j-1)
        TwoPivotBlockQuicksort(A, j+1, r)
        
def choosePivot(A, l, r):
    """Choose two pivot from A, if the first pivot is higher than the second pivot, then swap it."""
    if(A[l] > A[r]):
        A[l], A[r] = A[r], A[l]

def TwoPivotBlockPartition(A, l, r):
    n = r - l + 1 # Panjang dari Array
    if n <= 1:
        return (l, r)
    
    choosePivot(A, l, r)
    
    p, q = A[l], A[r]
    block = [0] * NUM_OF_BLOCKS
    i, j, k = l+1 , l+1, 1 
    np, nq = 0, 0
    while k < n-1:
        t = min(NUM_OF_BLOCKS, n-k-1)
        for c in range(t):
            block[nq] = c
            nq = nq + (q >= A[k + c + l])
        
        for c in range(nq):
            A[j + c], A[k + block[c] + l] = A[k + block[c] + l], A[j + c]
            
        k += t
        for c in range(nq):
            block[np] = c
            np = np + (p > A[j + c])

        for c in range(np):
            A[i], A[j + block[c]] = A[j + block[c]], A[i]
            i += 1
            
        j += nq
        np, nq = 0, 0
        
    A[i-1], A[l] = A[l], A[i-1]
    A[j], A[r] = A[r], A[j]
    return (i-1, j)

A = [-3, -6, -1, -2, -4, -5, -7, -8]
TwoPivotBlockQuicksort(A)
print(A)