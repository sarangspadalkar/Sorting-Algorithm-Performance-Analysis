from Generate_random_seq import gen_random_input
import time

def selection_sort(inp_array):
    N=len(inp_array)
    for i in range (N):
        min_index=i
        for j in range (i+1,N):
            if inp_array[min_index] > inp_array[j]:
                min_index = j
        temp=inp_array[min_index]
        inp_array[min_index]=inp_array[i]
        inp_array[i]=temp
    return inp_array