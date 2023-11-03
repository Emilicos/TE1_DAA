def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
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
                        
x =  [-3, -6, -1, -2, -4, -5]

merge_sort(x, 0, len(x) - 1)

print(x)