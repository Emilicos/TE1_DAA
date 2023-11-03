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
    
    for i in range(a): # iterasi mulai dari 0 karena indeks array dimulai dari 0
        L[i] = A[p + i] # Karena mulai dari 0, oleh karena itu, kita juga perlu menyesuaikan ini juga
    
    for j in range(b):
        R[j] = A[q + j + 1]
    
    L[a] = float("inf")
    R[b] = float("inf")
    
    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
                        
x =  [2, 7]

merge_sort(x, 0, len(x) - 1)

print(x)