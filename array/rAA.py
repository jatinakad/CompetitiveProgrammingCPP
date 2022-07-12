from multiprocessing.dummy import Array
from pipes import Template
from tracemalloc import start


def reverseArray(Array,Start,End):
    while(Start<End):
        # Array[Start],Array[End]=Array[End],Array[Start]
        temp = Array[Start]
        Array[Start] = Array[End]
        Array[End] = temp
        
        Start+=1
        End-=1

Array = [1,2,3,4,5,6]
print(Array)
print("reverse array is")
reverseArray(Array,0,5)
print(Array)

