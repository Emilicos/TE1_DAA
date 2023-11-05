import tracemalloc
import time
from quicksort_two_block_pivot import TwoPivotBlockQuicksort
from merge_sort import MergeSort
import copy
import numpy as np

types = ["small", "medium", "big"]
array_types = ["random", "sorted", "reversed"]

def SortDataUsingMergeSort(A, array_type):
    tracemalloc.start()
    start_time = time.time()
    MergeSort(A)
    end_time = time.time()
    # menggunakan peak memory
    used = tracemalloc.get_traced_memory()[1]/1024
    tracemalloc.stop()
    
    A_sorted = sorted(A)
    assert np.array_equal(A_sorted, A)
    
    print(f"Sorting Mergesort dengan array {array_type} berukuran {len(A)} menghabiskan {used:.10f} KB.")
    delta = (end_time - start_time) * 1000
    print(f"Sorting Mergesort dengan array {array_type} berukuran {len(A)} menghabiskan {delta:.10f} ms.")

def SortDataUsingTwoPivotBlockQuicksort(A, array_type):
    tracemalloc.start()
    start_time = time.time()
    # tidak disimpan di variabel agar waktu assigmment tidak dihitung
    TwoPivotBlockQuicksort(A)
    end_time = time.time()
    # menggunakan peak memory
    used = tracemalloc.get_traced_memory()[1]/1024
    tracemalloc.stop()
    
    A_sorted = sorted(A)
    assert np.array_equal(A_sorted, A)
    
    print(f"Sorting Two Pivot Block Quicksort dengan array {array_type} berukuran {len(A)} menghabiskan {used:.10f} KB.")
    delta = (end_time - start_time) * 1000
    print(f"Sorting Two Pivot Block Quicksort dengan array {array_type} berukuran {len(A)} menghabiskan {delta:.10f} ms.")

def main():
    print("Perbandingan Algoritma Two-Pivot-Block-Quicksort dan Merge Sort")
    print("="*100)
    
    for type in types:
        for array_type in array_types:
            A_merge_sort, A_quick_sort = [], []
            with open(f'dataset/{type}/{array_type}.txt', 'r') as file:
                A_merge_sort = [int(line.strip()) for line in file.readlines()]
                
            A_quick_sort = copy.deepcopy(A_merge_sort)
            
            # SortDataUsingMergeSort(A_merge_sort, array_type)
            
            SortDataUsingTwoPivotBlockQuicksort(A_quick_sort, array_type)

    return True

if __name__ == '__main__':
    main()