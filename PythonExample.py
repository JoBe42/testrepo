import random, time, copy
import numpy as np

# generate random list
randomlist = random.sample(range(0, 1000), 1000)

def selectionSort(unorderedlist):
    t1 = time.time()
    S = copy.copy(unorderedlist)
    # find minimum in S 
    for i in range(0, len(S)-1): 
        actmin = S[i]
        minind = i
        for j in range(i + 1, len(S)):
            # find the new minind for all j>i 
            if S[j] < actmin:
                actmin = S[j]
                minind = j
        S[i], S[minind] = S[minind], S[i]
    t2 = time.time()
    t = (t2-t1)*1000
    return S, t            
        
def bubbleSortFHU(unorderedlist):
    t1 = time.time()
    S = copy.copy(unorderedlist)
    for i in range(1, len(S)): 
        for j in range(len(S)-1, i-1, -1):
            if S[j] < S[j-1]:
                S[j], S[j-1] = S[j-1], S[j]
    t2 = time.time()
    t = (t2-t1)*1000
    return S, t


def bubbleSort(unorderedlist):
    t1 = time.time()
    S = copy.copy(unorderedlist)
    swap = 1
    while swap:
        swap = 0
        for i in range(0, len(S)-1):
            if S[i+1] < S[i]:
                S[i+1], S[i] = S[i], S[i+1]
                swap = 1                
    t2 = time.time()
    t = (t2-t1)*1000
    return S, t
 
def numpySort(unorderedlist,kind):
    t1 = time.time()
    S = np.sort(unorderedlist, kind=kind)
    t2 = time.time()
    t = (t2-t1)*1000
    return S, t

# print("Unsorted integers: ", len(randomlist), randomlist)
# print("SELECT-sorted duration: ", selectionSort(randomlist)[1])
print("BubbleFHU-sorted duration: ", bubbleSortFHU(randomlist)[1])
print("My-Bubble-sorted duration: ", bubbleSort(randomlist)[1])
print("NP-MERGE-sorted duration: ", numpySort(randomlist,"mergesort")[1])
print("NP-QUICK-sorted duration: ", numpySort(randomlist,"quicksort")[1])
print("NP-HEAP-sorted duration: ", numpySort(randomlist,"heapsort")[1])
