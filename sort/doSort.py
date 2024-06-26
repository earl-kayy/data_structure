from shellSort import *
from insertionSort import *
from quickSort import *

def do_sort(input_file):
    data_file = open(input_file)
    A = []
    for line in data_file.readLines():
        lpn = line.split()[0]
        A.append(lpn)

    for i in range(1000, 1010, 1):
        print(A[i], end = " ")
    print("")

    shellSort(A)
    insertSort(A)
    quickSort(A, 0, len(A)-1)

    for i in range(1000, 1010, 1):
        print(A[i], end = ' ')

    print("")

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    do_sort("./linkbench_short.trc")
    end = time.perf_counter()
    elapsed_time_us = (end-start)*1000
    print(f"Elapsed time: {elapsed_time_us:.2f} ms")