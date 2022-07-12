from multiprocessing.dummy import Array
from pandas import array


def reverseArray(Array,start,end):
    if start >= end:
        return
    
    Array[start],Array[end]=Array[end],Array[start]
    reverseArray(Array,start+1,end-1)

Array = [1,2,3,4,5,6]
print(Array)
reverseArray(Array,0,5)
print(Array)