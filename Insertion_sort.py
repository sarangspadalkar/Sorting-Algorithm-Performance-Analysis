from Generate_random_seq import gen_random_input
import time

def insertion_sort(inp_array):
    N=len(inp_array)
    for i in range (1,N):
        key_ele=inp_array[i]
        j=i-1
        while j>=0 and key_ele<inp_array[j]:
            inp_array[j+1]=inp_array[j]
            j-=1
        inp_array[j+1]=key_ele
    return inp_array