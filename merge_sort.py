import numpy as np

def MergeSort(A, p = None, r = None):
    if(p is None and r is None):
        p, r = 0, len(A) - 1
        
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

def Merge(A, p, q, r):
    a = q - p + 1
    b = r - q

    L = [0] * (a + 1)
    R = [0] * (b + 1)
    
    for i in range(1, a + 1):
        L[i - 1] = A[p + i - 1] # Index L dikurang 1, karena list L mulai dari 0
    
    for j in range(1, b + 1):
        R[j - 1] = A[q + j] # Index R dikurang 1, karena list L mulai dari 0
    
    L[a] = float("inf")
    R[b] = float("inf")
    
    i = 0 # i mulai dari 0 karena indeks array dimulai dari 0
    j = 0 # j mulai dari 0 karena indeks array dimulai dari 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
            

# Just testing result ...

def main():
    with open('dataset/big/random.txt', 'r') as file:
        A = [int(line.strip()) for line in file.readlines()]
    
    A_sorted = sorted(A)
    MergeSort(A)
    
    assert np.array_equal(A_sorted, A)
    print("Kedua array sama :D")
    
if __name__ == '__main__':
    main()       